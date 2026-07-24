# Notes for File Handling

Module 1 : Introduction to File Handling

A file is a place on disk where data is stored permanently.

    - stored in secondary memoery 
    - Data remains even after program stops
    - Used to store large data

    Example:

        - data.csv
        - student.txt
        - config.json
        - image.png 

Types of FIles:

    - Text File : Human Redable  Mode (t)
        - .txt
        - .csv
        - .json
        - .log

    - Binary Files : Not human Redable (Machine Format) Mode(b)

        - .jpg
        - .png
        - .mp3
        - .pdf
        - .exe

File FOrmats:

TXT:

- Simple text 


CSV 

id,name,age
1,Rahul,20

JSON 

{
    "name":"Rahul",
    "age":20
}


LOG 

System log 

XMl 

<name> Rahul </name>


How File Handling Works :

1. Open File 
2. Perform Operation (read/write)
3. Close file 


# Write a File 

f=open("demo.txt","w")
f.write("Hello Python")
f.close()

# Read a File 

f=open("demo.txt","r")
data=f.read()
print(data)
f.close()



Module 2 : File Paths & Location in Python 

    - A file path is the location of a file in your system.

    home/user/data.txt
    D://User/data.txt


    Types of File Path:

        1. Absolute Path (FULL PATH)

            - Comaplte path from root directory 

            - C:\Users\Anuj\Desktop\data.txt
            - /home/anuj/data.txt

            Advantage:

            - Always works 
            - No dependency on current folder 

            Disadvantage:

            - Not portable 

        2. Relative Path 

            - Path relative to current working directory 

            - File is in same folder as script 


        Note:

        .   Current Directory 

        ..  Parent Directory 


Check Current Directory:

import os 
print(os.getcwd())

change Directory:

os.chdir("/path/to/folder)



Module 3: Opening a File (open())

What is open()?


Open() is used to open a file so that python can intreact with it.

    - Before reading/writing -> FIle must be an opened 

    - It return a file object 

Syntax:

    file_object=open(file_name,mode)

    - f=open("data.txt","r") # r= read mode 


Parameter of open():

1. FIle Name 

    - Relative path 
    - Abosulte Path 

2. MOde 

    What operation you want to perform 

    - r -> read 
    - w -> write 

3. Encoding 

    f= open("data.txt","r", encoding="utf-8")

    f= file object : Interface to intreact with file :

        - Read
        - write 
        - Move Pointer 
        - Close file 

# Common Modes :

    Mode            Meaning 

    r               Read

    w               Write 

    a               Append 

    x               Create 


# FileNotFoundError 


if  os.path.exists("demo.txt"):
    f=open("demo.txt","r")



Module 4 : File Modes 


    - What operations you want to perform on the file.


    1. REad Mode(r)


        - f=open("data.txt",r)

        - Opening file for reading 
        - File Must exist 

        -------> If file not exists 
        -> FIleNotFOundError 


        -> Reading logs 
        -> Reading input data 
        -> Reading config 


    2. Write mode(w) 

        - f=open("data.txt",w)

        - Creates file if not exists 
        - If exists - Overwrite (Danger)


    3. Append Mode (a)

        - f=open("data.txt",a)

        - Adds data at end 
        - Doest not Overwrite 
        - Createes file if not exists 


    4. Create Mode (x)

        - Creates new file 
        - Error if file already exists 


# Module 5 : Closing Files & with statement 

1. Why closing a file is important ?

    - Allocate system resources 
    - Creates a connection with OS 

    if you dont close it:

        - Memory leak 
        - File lock issue 
        - Data may not be written completely 
        - System Performance issue 


    f=open("data.txt",w)
    f.write("Hello")
    # forget to close 


    # Closing a file 

    f.close() - syntax 


    f=open("data.txt",w)
    f.write("Hello")
    f.close()

    problem :

        - If error occures before close() 
            - File remains open 


    Solution : with open() 

    syntax:

    with open("file.txt","r") as f:
        data=f.read() 

    - File automatically closed after block 
    - Even if error occures 


# Multiple file handling with - with open()

    with open () as f1,open() as f2:
        data=f1.read()
        f2.write(data)

# Exception Handling with File 

try:
    f=open("data.txt","r")
    data=f.read()
finally:
    f.close() 


# Module :6 

Reading files in Python :


with open("employee.txt","r",encoding="utf-8") as f:
    data=f.read() # reads file content 
    print(data)


Mains ways to read the file:

1. read() 
    - It reads the entire file contant at once and returns it as a single string

    When to use:

        - file is small 
        - You want whole content at once 
        - config/text file 
    
    problem :

        - If file is very large, read() can consume a lot of memory

2. read(size)

    - This reads only a fixed number of charcters.

    data = f.read(5)
    
    with open("employee.txt","r",encoding="utf-8") as f:
    data=f.read(6) # reads file content 
    print(data)

    ----------> 101,Jo

    Use cases:

        - you want chunk based reading 
        - file very large 
        - controlled reading 



3. readline()

    line = f.readline()
    

    with open("employees.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()

    print(line1)
    print(line2)

    You may notice an extra blank line while printing. That happens because each line already contains \n.


    - It reads one line at a line 

    Useful when:
	•	you want line-by-line processing
	•	you only need first line or few lines

4. readlines()

    lines = f.readlines()

    It reads all lines and returns a list of strings.

    with open("employees.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

    with open("employees.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

    output:  ['101,John,5000\n', '102,Alice,7000\n', '103,Bob,3000\n']


    Use case

Useful when:
	•	file is small
	•	you want line list directly

Problem

Not good for very large files because it loads everything into memory.

Best method: loop through file

This is the most commonly used approach in real projects.

with open("employees.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

Why this is best
	•	memory efficient
	•	simple
	•	clean
	•	works for large files
	•	used in production systems


Understanding strip()

When reading lines, they often end with newline character \n.

with open("employees.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

    This may print extra blank lines.
    line = line.strip()

    What strip() removes
	•	leading spaces
	•	trailing spaces
	•	newline \n

Reading file and splitting data

Suppose file contains:

101,John,5000
102,Alice,7000

You can read and split like this:

with open("employees.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        parts = line.split(",")
        print(parts)

output 

['101', 'John', '5000']
['102', 'Alice', '7000']


# Module : 7
Writing Files in Python 


    with open ("file_name.txt","w",encoding="utf-8") as f:
        f.write("Hello Python")

open - open files 
"w" - write mode 
f.write - writes content 
with closes file automatically 


write():

syntax:

    f.write(data)

    It writes a string into a file.

    -- write() only writes strings 


Writing multiple lines 

    with open ("file_name.txt","w",encoding="utf-8") as f:
        f.write("hello python\n")
        f.write("Welcome to file handling in python")
        f.write("This is a new line\n")
        f.write("This is another line")


    # Note - Python does not automatically add a new line when using write()

    So if you want each record on sepearte line add \n.


# writing inside loop 


    name=["john","Alice","Bob"]
    names=["alice","bob","charlie"]
with open ("file_name.txt","w",encoding="utf-8") as f:
    for name in names:
        f.write(name+"\n")


# Writing processed file data 

employee=[
    {"id":101,"name":"john","salary":5000},
    {"id":102,"name":"Alice","salary":9000}
]

with open ("file_name.txt","w",encoding="utf-8") as f:
    for emp in employee:
        line=f"{emp['id']},{emp['name]},{emp['salary']}\n"
        f.write(line)


# writelines() 

    f. writelines(list_of_strings)





# module 8 

    Appending to the files 


    What is append mode:

        - Append mode (a)

        - Add new data at the end of the file 
        - Existing data not removed 


        with open ("file_name.txt","a",encoding="utf-8") as f:
            f.write("new data\n")


diffrence : write(w) vs append(a) mode 

                    write(w)            append (a)

- Exising data      Delete              preserved 

- New data          written fresh       Added at last 

- File Exists       Overwrite           Used as is 

- file not exists   Created             created 



# Important Behavior of append Mode :

    - Pointer is laways at the end. 

    what is file pointer?

        - A file pointer (cursor) is a position indictor inside file.

        - It tells python where to read/write next 


        Hello Word 

        Hello world
        012345678910

        - Pointer moves from left to right 

    - Default pointer behavior :

        - First read- pointer moves 
        - second read - continue from previous pointer 

    

    # tell() 

        f.tell() # Returns current pointer position 

    with open ("file_name.txt","r",encoding="utf-8") as f:
    print(f.read(8))
    print(f.tell()) # 8 

    - Pointer is now at position 8 


    # seek() - Move pointer 

        f.seek(postion)

        advance:

            f.seek(offset,whence)

            whence values 

            0       Beginning (default)

            1       current

            2       End of file 


            with open ("file_name.txt","r",encoding="utf-8") as f:
                #print(f.read(5))
                f.seek(-5,2)
                print(f.read())


        Output:

            UnsupportedOperation                      Traceback (most recent call last)
            Cell In[139], line 3
            1 with open ("file_name.txt","r",encoding="utf-8") as f:
            2     #print(f.read(5))
            ----> 3     f.seek(-5,2)
            4     print(f.read())

            UnsupportedOperation: can't do nonzero end-relative seeks



        Questions : Why does seek(-5,2) fail in text mode:


        Answer : Because text mode is not byte-precise due to encoding, python restricts end relative negative seek 
        to perform such operations we need to use binary mode 


   




    - Moves pointer to specific location 

        with open ("file_name.txt","r",encoding="utf-8") as f:
        f.seek(8)
        print(f.read(4))


    Important :

        - Where reading starts 
        - where writing heppens 

    Reset seek:

        seek(0)

# pointer in write mode:


with open ("file_name.txt","w",encoding="utf-8") as f:
   f.write("hello)
   print(f.tell())



# Module - 9

File & Directory Operations (os, shutil, pathlib)

This module is used everywhere in Data Engineering, DevOps, ETL pipelines, AWS, automation scripts.

1. Why This Module is Important

In real projects, we don’t just read/write files. We also:
	•	create folders
	•	move files
	•	delete files
	•	check if file exists
	•	list files in directory
	•	rename files
	•	automate file pipelines

This is where os, shutil, and pathlib come in.

import os 
---------------

Get current directory : print(os.getcwd()) #/Users/anujshahdeo/Documents

List FIles in directory : print(os.listdir()) #['employees.txt', 'system.log', 'output.txt']

Create Folder : os.mkdir("new_folder")

Create Nested Folder: os.makedirs("data/output/logs")

Remove file : os.remove("output.txt")

Remove Folder: os.rmdir("new_folder") # only works if empty 

Rename file : os.rename("old.txt", "new.txt")

Check File Exists : os.path.exists("employees.txt")


Check file or Directory :

os.path.isfile("employees.txt")
os.path.isdir("data")



import shutil   (copy, move, delete folders )


Copy File : 
shutil.copy("employees.txt", "backup.txt")

Move File :
shutil.move("employees.txt", "archive/employee.txt")

Copy Entire Folder : 
shutil.copytree("data", "backup_data")

Delete folder - Deletes Folder even if not empty 
shutil.rmtree("data")




from pathlib import Path 

Create Path object 
p = Path("employees.txt")

Check Exists:

p.exists()

Check File FOlder:

p.is_file()
p.is_dir()

Create Directory:
Path("data/output").mkdir(parents=True, exist_ok=True)

List Files:

for file in Path(".").iterdir():
    print(file)

Get file extension:

p.suffix

Get file Name:

p.name

Read File:

p.read_text()

Write File:

p.write_text("Hello World")


Mode            Description             File_Exists?           Pointer

r                  Read                    Must exists          start
w                  write                   Overwrites           start
a                  append                  Create if not exist  End
r+                 Read + Write            Must Exist           start
w+                 Write + read            Overwrites           start
a+                 Append+Read             Creates if not exists End 
rb                 Read binary             Must exist           Start   
wb                 Write Binary            Overwrites           start
ab                 append binary           Creates              End
rb+                Read/write binary       must exists          start
wb+                Write/REad binary       Overwrite            Start
ab+                append/read ninary      Creates              End 



















































        


