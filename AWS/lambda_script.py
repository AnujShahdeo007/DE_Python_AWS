import boto3
import json
import csv
import io
import os
import logging
from datetime import datetime, timezone
from botocore.exceptions import ClientError

# --------------------------------------------------
# Logger setup
# --------------------------------------------------
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# --------------------------------------------------
# AWS clients
# --------------------------------------------------
s3 = boto3.client("s3")

# --------------------------------------------------
# Environment variables
# --------------------------------------------------
PROCESSED_PREFIX = os.getenv("PROCESSED_PREFIX", "processed/")
FAILED_PREFIX = os.getenv("FAILED_PREFIX", "failed/")
REPORT_PREFIX = os.getenv("REPORT_PREFIX", "reports/")


def lambda_handler(event, context):
    """
    Manual Lambda entry point.
    Expected event:
    {
        "bucket": "bucket-name",
        "input_prefix": "input/"
    }
    """

    logger.info("Lambda execution started")
    logger.info("Input event: %s", json.dumps(event))

    bucket = event.get("bucket")
    input_prefix = event.get("input_prefix", "input/")

    if not bucket:
        raise ValueError("Bucket name is required in event")

    summary = {
        "bucket": bucket,
        "input_prefix": input_prefix,
        "total_files": 0,
        "success_files": 0,
        "failed_files": 0,
        "files": []
    }

    try:
        files = list_s3_files(bucket, input_prefix)
        summary["total_files"] = len(files)

        if not files:
            logger.warning("No files found under prefix: %s", input_prefix)
            return build_response(200, summary)

        for file_key in files:
            result = process_single_file(bucket, file_key)
            summary["files"].append(result)

            if result["status"] == "SUCCESS":
                summary["success_files"] += 1
            else:
                summary["failed_files"] += 1

        logger.info("Lambda execution completed successfully")
        logger.info("Final summary: %s", json.dumps(summary))

        return build_response(200, summary)

    except Exception as e:
        logger.exception("Lambda execution failed")
        return build_response(500, {"error": str(e)})


def list_s3_files(bucket, prefix):
    """
    List all files from given S3 prefix.
    Skips folders.
    """

    logger.info("Listing files from s3://%s/%s", bucket, prefix)

    files = []

    try:
        paginator = s3.get_paginator("list_objects_v2")

        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]

                if key.endswith("/"):
                    continue

                files.append(key)

        logger.info("Total files found: %s", len(files))
        return files

    except ClientError as e:
        logger.exception("Failed to list files from S3")
        raise e


def process_single_file(bucket, file_key):
    """
    Process one S3 file.
    """

    logger.info("Processing file: s3://%s/%s", bucket, file_key)

    file_name = file_key.split("/")[-1]# s3://bucket/input/file.csv -> file.csv
    extension = file_name.lower().split(".")[-1]

    result = {
        "file_name": file_name,
        "source_key": file_key,
        "status": None,
        "record_count": 0,
        "message": None,
        "processed_at": datetime.now(timezone.utc).isoformat()
    }

    try:
        content = read_s3_file(bucket, file_key)

        if not content.strip():
            result["status"] = "FAILED"
            result["message"] = "Empty file"
            move_file(bucket, file_key, FAILED_PREFIX + file_name)
            write_report(bucket, result)
            return result

        if extension == "csv":
            record_count = process_csv(content)

        elif extension == "json":
            record_count = process_json(content)

        elif extension == "txt":
            record_count = process_txt(content)

        else:
            result["status"] = "FAILED"
            result["message"] = f"Unsupported file type: {extension}"
            move_file(bucket, file_key, FAILED_PREFIX + file_name)
            write_report(bucket, result)
            return result

        result["status"] = "SUCCESS"
        result["record_count"] = record_count
        result["message"] = "File processed successfully"

        move_file(bucket, file_key, PROCESSED_PREFIX + file_name)
        write_report(bucket, result)

        logger.info("File processed successfully: %s", file_name)
        return result

    except Exception as e:
        logger.exception("File processing failed: %s", file_name)

        result["status"] = "FAILED"
        result["message"] = str(e)

        try:
            move_file(bucket, file_key, FAILED_PREFIX + file_name)
            write_report(bucket, result)
        except Exception:
            logger.exception("Failed while moving failed file or writing report")

        return result


def read_s3_file(bucket, key):
    """
    Read S3 file as text.
    """

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read().decode("utf-8")
        return content

    except ClientError as e:
        logger.exception("Unable to read file from S3: %s", key)
        raise e


def process_csv(content):
    """
    Validate and count CSV rows.
    Header is excluded from count.
    """

    csv_file = io.StringIO(content)
    reader = csv.reader(csv_file)

    rows = list(reader)

    if len(rows) <= 1:
        raise ValueError("CSV file has no data rows")

    header = rows[0]
    data_rows = rows[1:]

    logger.info("CSV header: %s", header)
    logger.info("CSV row count: %s", len(data_rows))

    return len(data_rows)


def process_json(content):
    """
    Validate and count JSON records.
    Supports JSON array or single JSON object.
    """

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")

    if isinstance(data, list):
        record_count = len(data)
    elif isinstance(data, dict):
        record_count = 1
    else:
        raise ValueError("JSON must be object or array")

    logger.info("JSON record count: %s", record_count)
    return record_count


def process_txt(content):
    """
    Count non-empty lines in text file.
    """

    lines = [line for line in content.splitlines() if line.strip()]

    if not lines:
        raise ValueError("Text file has no valid lines")

    logger.info("TXT line count: %s", len(lines))
    return len(lines)


def move_file(bucket, source_key, destination_key):
    """
    Move file inside S3 using copy + delete.
    """

    logger.info("Moving file from %s to %s", source_key, destination_key)

    try:
        s3.copy_object(
            Bucket=bucket,
            CopySource={"Bucket": bucket, "Key": source_key},
            Key=destination_key
        )

        s3.delete_object(
            Bucket=bucket,
            Key=source_key
        )

        logger.info("File moved successfully")

    except ClientError as e:
        logger.exception("Failed to move file")
        raise e


def write_report(bucket, result):
    """
    Write file-level processing report to S3.
    """

    file_name = result["file_name"]
    report_name = file_name.rsplit(".", 1)[0] + "_report.json"
    report_key = REPORT_PREFIX + report_name

    logger.info("Writing report: s3://%s/%s", bucket, report_key)

    try:
        s3.put_object(
            Bucket=bucket,
            Key=report_key,
            Body=json.dumps(result, indent=4),
            ContentType="application/json"
        )

        logger.info("Report written successfully")

    except ClientError as e:
        logger.exception("Failed to write report")
        raise e


def build_response(status_code, body):
    """
    Standard Lambda API-style response.
    """

    return {
        "statusCode": status_code,
        "body": json.dumps(body, indent=4)
    }