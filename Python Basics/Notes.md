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




***************************************************************************************************************************
*                                                     Operators                                                        *
***************************************************************************************************************************

Operators are symbols/keywords used to do action on values(Operands)

ex:     a+b ---> + Operator 
        a,b ----> Operands 

1. Airthmetic Operators 
-------------------

Operators                   Meaning             Example                 Result 
    +                       Addition            5+2                        7
    -                       Suntraction         5-3                        2 
    *
    /                       True division       5/2                        2.5 # Always resturn Float
    //                      floor division      5//2                       2
    %                       modulus (Remainder) 5%2                        1
    **                      Power               5**2                       25


Important Points 
----------------
- / always give a float value 
- // always gives a floor value (rounded value)
  -5 // 2 is -3 (Because floor of -2.5 is -3)
- % sign follows divisor rule in python : -5%2 is 1 

2. Comaprision Operator 
------------------------

Operator        Meaning                 Example 
==              equal
!=              not equal
>               greater
<               less
>=              greater or equals
<=              less or equals 


Key concepts 
------------
Comparision return a boolean : True or False 
x=10 
print(5< x < 20)  # True

3. Assignment Operators 
------------------------

Operator            Meaning                 Example 
=                   assign 
+=                  add then assign 
-=.                 suntract then assign
*=
/=
//=
%=
**=

Important points 
-----------------
- For int,str,tuple (Immutable) : x +=1 makes a new object 
- for List (mutable): lst += [1] Changes the same list

4. Logical Operators 
--------------------

Operator            Meaning 
and                 both conditions must be true 
or                  at least one true 
not                 flip boolean 

a=0 
print(a and 10) # 0 (stops early because a is false)
print(a or 10) #  10 (return first true value)

Python returns one of the operands, not always True/False.
In if, it behaves like boolean 


Bitwise Operators 
-----------------
Operators               Meaning 
&                       AND
'                        '
^                       XOR
~                       NOT
<<                      left shift
>>                      right shift


a=5 # 0101
b=3 # 0011
print(a&b) # 1 (0001)
print(a^b) # 6 (0110)


6. Memebership Operator
-----------------------

    In, not in - Used to check presence 

    print ("a" in "datascience") # True
    print( 3 in [1,2,3]) # true
    print (3 not in [1,2,3]) # False 

7. Identity Operator 
---------------------

    is , is not - Checks same object in memory,Not value equality 

    a=[1,2]
    b=[1,2]

    print(a==b) # True (same values)
    print(a is b) # False ( diffrent object )


***************************************************************************************************************************
*                                                     Input/Output                                                       *
***************************************************************************************************************************

What Is input and Output (I/O) in programming?
- Input : Take data from outside(User,File,API,Db,sensor)
- Process : Apply logic 
- Output : Show/save a result (Screen, file,DB,API)

Console Input : input()
Consule Output : print()

1. What print() actually does?
- print() - sends text to standarad output (stdout) - usually the terminal/console 

print("Hello")

    - Python evalutes "Hello"
    - Convert it into string represenatation (already string)
    - write it to stdout
    - add a new line by default /n

sep (separator) - 

By default 
    - sep=" "
    print(1,2,3) --> 1 2 3 
    print (1,2,3, sep=",") --> 1,2,3

    print("2026","02","02", sep="/") -> 2026/02/02


   - end -> Controls what happens at the end

   By Default: end="\n" -> Means print ends with newline

   print("hello", end=" ") 
   print("world)
   -------------> hello world 

   Formatted Priniting :
   when we print,
    - mix test + variables 
    - control statement 
    - align output 
    - formate dates,numbers and logs 

f-STRING (Best & Modern way ) 

-- python 3.6 

Syntax 
------

f"some text {}"

Name= "Priya"
age=10 

print(f"Hello this my name{name}.      {name * age}.        this my age "). --> Hello this my namePriya.      10.        this my age 

How it works internally 
----------------------

1. Python sees f before string 
2. Evalutes expression inside {}
3. Converst result to string 
4. Insert into final string 

a=10
b=20 
print(f"Sum is {a+b}") - Sum is 30

2. Formatting numbers (DECIMALAS)
---------------------------------
pi=3.1415926
print(f"Pi value {pi:.2f}") --> 3.14 

3. Padding with width 
---------------------
x=5 
print(f"{x:04}") - 0005


print(True)
print(False)


----------------------------------------INPUT ------------------------------------------------------
input() reads a line from standard input (stdin) usually from keyboard 

name=input("Enter you name: ") # Prompt - The string you pass into input() is just a prompt message 
name= priya 

Rule:
input() always  returns a string 

INT 
----
age=int(input("Enter age: ")) # Typecasting
print(age+1)

FLOAT
-----


Comment
-------
To explain code logic 
To make code redable 
To leave notes for youself or teammates 

Single line 
----------
# this ia a comment 
x=5 # this comment 

Multipline comment 
------------------
#
#
#
#

Triple quotes 
-------------
"""

"""












    
