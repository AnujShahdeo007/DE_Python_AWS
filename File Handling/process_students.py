from datetime import datetime
INPUT_FILE="students.txt"
OUTPUT_FILE="output.txt"
LOG_FILE="app.log"

def write_log(level,message):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message=f"{timestamp}, {level}, {message}\n"
    with open(LOG_FILE,"a",encoding="utf-8") as log_file:
        log_file.write(log_message)

def get_marks(marks):
    if marks>=90:
        return"A"
    elif marks >=75:
        return "B"
    elif marks >=40:
        return "C"
    else:
        return "Fail"
def get_result(marks):
    return "Pass" if marks>=40 else "Fail"

def process_students():
    total_records=0
    success_records=0
    failed_records=0

    write_log("INFO","Process Starated")

    try:
        with open(INPUT_FILE,"r",encoding="utf-8") as infile,open(OUTPUT_FILE,"w",encoding="utf-8") as outfile:
            for line_number,line in enumerate(infile,start=1):
                total_records+=1
                line=line.strip()

                if not line:
                    write_log("WARNING",f"Skipping empty line at line {line_number}")
                    continue
                write_log("INFO",f"Reading Line {line_number}")
                parts=line.split(",")

                if len(parts) !=3:
                    failed_records+=1
                    write_log("ERROR",f"Invalid format at line {line_number}:{line}")
                    continue
                student_id,name,marks=parts

                try:
                    marks=int(marks)
                except ValueError:
                    failed_records+=1
                    write_log("ERROR",f"Invalid marks at line {line_number}:{line}")
                    continue
                result=get_result(marks)
                grade=get_marks(marks)
                output_line=f"{student_id},{name},{marks},{result},{grade}\n"
                outfile.write(output_line)
                success_records+=1
                write_log("INFO",f"Successfully processed student_id={student_id}")
        write_log("INFO",f"Process Completed. Total={total_records},success={success_records},Failed={failed_records}") 
        print("Processing completed successfully")  
        print(f"Total records:{total_records}")
    except FileNotFoundError:
        write_log("ERROR",f"Input File not found: {INPUT_FILE}")    
        print(f"Error: Input file {INPUT_FILE} not found")
    except Exception as e:
        write_log("ERROR",f"Unexpected Error: {str(e)}")    
        print(f"Error",f"Unexpected Error : {str(e)}")

if __name__=="__main__":
    process_students()