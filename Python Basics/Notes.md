# Notes for Python Basics

What Is Python?

- Programming Language 
- Simple (like Engilish )
- Used In 
    - Web Applications 
    - Data Enginerring 
    - AI/ML 
    - Automation 
    - Testing 

How Python Runs a Program 
-------------------------
x=10
y=20
print(x+y)

Step 1: Python Interprepter Starts 
    - When you click Run - The Python Interpreper Starts 
        - The interpreter is repsonsible for: 
            - Reading code 
            - checking rules 
            - Excuting instractions 

step 2 : Read code line by line 
    - Python reads the program from top to bottom 

    Order Matters 
    -------------
    Line 1: x=10
    line 2: y=20
    line 3: print(x+y)

Step 3 : Tokenization ( Breaking code )

    - Python breaks each line into token( samll meaningfull part)

    x=10 

    Token 

    x = 10 
 Step 4: Stantax Checking 

    - Are keywords are correct 
    - Are brackts are correct 
    - Are quotes are correct 

    -----> Syntax Error 

Step 5: Convert to bytecode

    - If syntax correct 
        - Python converts code into bytecode 
        - Bytecode is a low level instarction not machine code 
        
Step 6: Excution 

Line by line 


***************************************************************************************************************************
*                                                      Variables                                                          *
***************************************************************************************************************************


Variables :

    - A variable is a name you give to a value so you can use it again.

Example 

name="Nilam"
age=20

Why do we need vairable:

Without variable you'd reperat value again and again 

print("Nilam")
print("Nilam)

with Variable
---------------

name="Nilam"

print(name)
print(name)

Common Mistakes 
---------------
1. USing variables before defining 

2. Case Sensitive 
    Name="A"
    print(name) #Name Error

3. Wrong Naming 

    1name= --------> Cannot start with number 
    my-name="A" ------means - (subtraction)   ###my_name

4. Allowed 

    my_name 
    _name
    name1

Practice Questions 
-------------------

1. Store your name and age and print my name is ----- and age is ------

***************************************************************************************************************************
*                                                      Datatypes                                                          *
***************************************************************************************************************************

What is dataype?

A data type tells python what kind of value a variable is holding.

x=10 # Number 
y="Hello" #text 


## 

Python is Dynamically Typed 

This means 

    - We dont declare type explicitly 
    - Python decides type at runtime 

Built- in data type 
-------------------

int     Integer     10,-5 

    - Whole number 
    - No decimal 


float   Decimal     10.5

str     String      "Hello"

bool    Boolean      True/False 



Categories of datatype 
-----------------------

1. Numeric 

    Interger (int)
        - Whole Numbers 
        - No decimal value 

        (-10,0,5,100)

        Charactriestics:
            - Can be positive or negative 
            - No Size Limit (Python handles big integers)
            - Immutable ( Cannot be changes in place )

    Floating (Float)

        - Numbers with decimal values 

        (3.14,10.5,-2.0)

        Charctristics 
        -------------
            - Immutable 
            - Can cause precision issues 

    Complex
    --------

    Used in scientific calculations 
    3+4j 


2. Sequence 

    String (str)
        - A sequence of character 
        - Used to store text 

        "Hello" "world"
    
    3. Creating String (All Ways )
    -------------------------------

    - Single quotes/Double quotes 
      b="Hello"
      a='hello'

    - Triple Quotes 
      msg="""Hello Team Today we will learn python"""
      print(msg)

    - Str() conversion

        x=100 ---> Type(x)---> int 
        s=str(x)---> type(s) ---> str 

    - Escape Charcter 
        print("he said\"Hi\"") -> \" -> Tells Python : " This Quote is a part of string, not the end"
        print("Line1\nLine2")--> Move cursor to next line 
        print("Tab\tSpace") --> Insert a TAB space 
    - Raw String 

    1. What is Indexing 
    -------------------
    Indexing means - Accessing a single element from a sequence using its position.

    Sequence you can index:
        - str(string)
        - List 
        - Tuple 
        - range

    s="python"
    print(s[0]) -> p
    print(s[1]) -> y

    Negative Indexing 
    ----------------
    print(s[-1]) -> last (n)
    print(s[-2]) -> o

    print(s[10]) ---> IndexError
    print(s[-10]) ---> Index Error 


    2. What Is Slicing 
    ------------------

    Slicing means : Extarcting a sub sequence(a piece) from a sequence.

    Slice Syntax 
    -------------

    seq[start:end:step]

    start: Where to begain (included)
    stop : Where to end (Excluded)
    step: How many to jump each time 

    Rule: 1 Stop is Excluded 

    s="Python"

    print(s[0:2])

    Key Rule:

    End index is always exclusive python places it one position outside the valid range:

    Direction           End Boundary
    forward             len(s)
    backward            -(len(s)+1)

    s="python"
    Python uses -7 as a end boundary becasue slicing stops before the index and -7 lies just outside the first valid negative index -6.

    Rules 
        - Written inside quotes 
        - Quotes define text and not value 
    characteristics 
        - Ordered 
        - immutable 
        - Can be indexded 

    Internelly 
        - Each charcter stored sequentially 
        - String object created in memory 
    
    List 

    Tuple 

    


3. Boolean

4. Set 

5. Mapping 

6. None Type 
-----------------------------------------------------------------------------------------------------------------------------
Type Casting 
-------------------'
Type casting means converting one data type to another. 

2 Types of type casting 
-----------------------

    1. Implicit Type casting (Automatic)
        -  Python automatically converets samller types into larger types to avoid data loss 

    2. Explicit Type casting (Manual)
        - Programmer explicitly converts a type using buitin functions.

1. Implicit Type casting (Automatic)
    a=10 
    b=2.5 #float

    c=a+b 
    print(c) 


2. Explicit Type casting (Manual)

    functions           converts to 
    int()               interger 
    float()             float
    str()               string
    bool()              boolean
    list()              List
    tuple()             tuple
    set()               Set
    dict()              Dictionary 


    2.1 int() casting 

    
