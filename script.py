import json
import boto3
from urllib.parse import unquote_plus

# ================================
# HARDCODED CONFIGURATION
# ================================

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:123456789012:s3-file-upload-alerts"  

# ================================
# AWS CLIENT
# ================================

sns = boto3.client("sns")

# ================================
# LAMBDA HANDLER
# ================================

def lambda_handler(event, context):
    print("Lambda triggered by S3 event")
    print(json.dumps(event))

    try:
        records = event.get("Records", [])
        messages = []

        for record in records:
            s3_info = record.get("s3", {})
            bucket_name = s3_info.get("bucket", {}).get("name")
            object_key = s3_info.get("object", {}).get("key")

            if object_key:
                object_key = unquote_plus(object_key)

            msg = (
                f"New file uploaded in S3\n\n"
                f"Bucket Name : {bucket_name}\n"
                f"File Path   : {object_key}"
            )

            messages.append(msg)

        if not messages:
            print("No S3 records found")
            return {"statusCode": 200, "body": "No records"}

        final_message = "\n\n------------------\n\n".join(messages)

        # ================================
        # PUBLISH TO SNS
        # ================================

        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New S3 File Uploaded Alert",
            Message=final_message
        )

        print("SNS Message Sent:", response)

        return {
            "statusCode": 200,
            "body": json.dumps("Email notification sent successfully")
        }

    except Exception as e:
        print("Error occurred:", str(e))
        raise e
