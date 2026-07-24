# Notes for Control Statements
***********************************************************************************************************************************
*                                                    Control Statement                                                            *
***********************************************************************************************************************************

A control statement decides which code should run based on which condition.

    - if this condition is true --> do this 
    - Otherwise -> Do something else 

if-else
--------
    if condition:
        #code runs if condition is True 
    else:
        # code runs if condition is false 

    Rules:
        - If condition must give True or False 
        - :(colon) is mandatory
        - Indentdation (spaces) is mandatory
        - else never has a condition 
 
    age=20
    if age >=18:
        print("You can vote")
    else:
        print("You cannot vote")
    
Multiple conditions using logical Operators 
-------------------------------------------
and 
----
age=25
citizen=False
if age>=18 and citizen ==True:
    print("Eligible for vote")
else:
    print("Not Eligible")


or 
---

day="Sunday"
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working Day")


Elif (Else-if)
--------------

if condition 1:
    --------
elif condition 2:
    ---------
elif condtion 3:
    ---------
else:
    -------

Flow:
    - Python checksw from top to bottom 
    - First True block execute 
    - Remaning block ignored 

Rule:
    - Only one block executes
    - Order matters 
    - Python stops at first True

marks=95

if marks >=90:
    print("Grade A")
elif marks >=60:
    print("Grade B")
else:
    print("Fail")



nested if
--------
Nested: Inside 
    nested if -> if inside another if 

Why do we need nested if?
    Becasue sometimes one decision depends on another decision.

if condition 1:
    if condition 2:
        #code 
    else:
        #code 
else:
    #code 


loops
------
1. What is a Loop and why we need it?
    - A loop repeats a block of code multiple times.

    for i in range(1,6):
        print(i)

Why Loops are used:
    - Reapting tasks (Processing file,Logs,rows)
    - Working with collection (List,set,dict,string)
    - Data pipeline (records,retries)

- 2 types of loop:
---------------------

A. FOR LOOP 
    - Use when you know the items you want to iterate(list,range,string,dict,file line)

B. WHILE LOOP
    - USe when you repeat until a condition becaomes False.


for i in [0,1,2,3,4]:
    print(i)


break/continue
--------------
Break:
    - Immediately exists the loop.
    - Control moves outside the loop
    - No more iteration happen.
Continue:
    - Skip the rest of the current loop body.
    -Goes into next iteration
    - Loop does not stop
