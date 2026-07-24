# Notes for Functions

function definition
--------------------
A function is a named block of reusable code that performs a specific tasks.
    - Write logic once,use it multiple times 

Why functions are important:
    - Avoid repeating code 
    - Make code readable 
    - Easy debigging 
    - Organized structure 
    - Reusability

Syatax:
    def function_name():
        #function body 

    def greet(): 
        print("Hello")

Parameter:
    Parameters are variable that receives value when the function is called.

    def function_name(parameter1,parameter2......)
        use paramter 

Arguments
--------
Arguments are the actual values passed when calling the function.

    funcation_name(value1,value2)

Rule:
    - parameter             - Variable in function defination 
    - Argument              - Actual value passed to function 


Question : Can we have the same function name with diffrent number of paramenter in python?

         - No, Python does not support function overloading like java/c++.
    
What is function overloading?
    - Same function name
    - Diffrent number or type of paramenters 

For example (java,c++)
----------------------

add(int a,int b)
add(int a,int b, int c)

----> Note: Second function in python --> Overwrites the first one 
            - Python keeps only latest definition.



def add(a,b,c=None):
    if c is None:
        print(a+b)
    else:
        print(a+b+c)




Senario                               use 

few optional parameters             Default args 
Unknow number of input              *args 
Name dynamic input                  **kwargs
Mixed logic                         Conditional    



return
-------
    - Sends a value back to the caller 
    - Ends the function execution 
    - Makes the function reuabale in logic 

def add(a,b,c):
    print(a+b+c)

result=add(10,20,30)
print(result)

Output
------
60
None

Why None:
    - print() just display output 
    - Function return Nothing by default 
    - Python returns None 

def add(a,b):
    return a+b
    print("This will not be printed") 

Flow:
-----
    - Function is called
    - return executes 
    - Function Stops immediately 
    - Control goes back to caller 



lambda
------

def add (a,b):
    return a+b


add(2,3)

syntax 
-------

lambda arguments : expression 

lambda a,b: a+b 

Rule:
    - Only one expression allowed 
    - No multiple statements 
    - Automatically return value 
    - Short logic 

Why do we use Lambda 
-------------------
    - Small temporary function 
    - Quick calculation 
    - inside map(),filter() 

Insted of creating full fun for small logic - Use lambda 

recursion


Basic 
------
add=lambda x,y:x+y
print(add(5,3))

map(function )

square=lambda n:n*n
print(square(5))

Lambda with Conditional statement 
---------------------------------

check=lambda x : "Even" if x%2==0 else "Odd"
print(check(7))

check =lambda x : "greater then " if x>45 else " "

nums=[1,2,3,4]
result= list(map(lambda x:x*10,nums))
print(result)

Nested IF lambda
----------------

if condition 1:
    result 
elif condition2:
    result
else:
    result3 

result=lambda x : result if condition1 else result2 if condition 2 else result 


def check(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"


check=lambda n : "Positive" if n>0 else "Negative" if n<0 else "Zero"

print(check(-5))


Q.1

    marks >=90 -> Distinction 
    marks >=60 -> Pass 
    else - Fail 

Q.2 
    salary>50000 AND rating >= 4 -> Bonus 
    salary > 50000 -> Review 
    Else -> No bonus 

bonus= lambda s,r : "Bonus" if s>50000 and r > 4 else "Review" if s > 50000 else "No Bonus"


Nested Lambda 
-------------

lambda x :(lambda y : something)


multiply=lambda x :(lambda y : x*y)
print(multiply(5),(3))


Nested lambda with Conditional 
-------------------------------

If x > y -> Bigger 
Else -> Smaller 

compare= lambda x : lambda y : "Bigger" if x>y else "Smaller"

cal= lambda x : lambda y : lambda z : x+y+z
print(cal(1)(2)(3))


  salary>50000 -- > check rating 
  rating >=4 -> Bonus 
  Else -> No bonus 


  bonus = lambda s : lambda r : if s >50000 else 


Recursion 
---------
    - Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

    - Instead of repeating with loops the function breaks the problem into smaller sub problems.

    Recursion - Solve big problem --> By solving smaller same problem 

    Base case:
        Stopping Condition 
            - Stop infinite recrusion 

        Without base case: Recursion Error : Maximum recusion depth exceeded 

    Recursive Case:
        - Reduce problem size 
        - return n+ total(n-1)



def countdown(n):
         return 
    print(n)
    countdown(n-1)


Factorial 
---------
5!= 5*4*3*2*1

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

count digit 
-----------

def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
print(count_digits(12345))

def count_digit_loop(n):
    count=0
    while n>0:
        count +=1
        n=n//10
    return count 
 if n==0:
  