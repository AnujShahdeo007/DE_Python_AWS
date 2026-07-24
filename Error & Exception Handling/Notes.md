# Notes for Error & Exception Handling

What is Error?

An error ia a problem in the program that prevent the program from running.

Erros usually occur due to incorrect code, syntax --> By programmer 

Types of Error 

1. Syntax Error 

2. Runtime Error :
    - Runtime Error occures while program is running 
    - Called Exception

3. Logical Error 
    - Logical occuer when program runs sucessfully but gives incorrect result


What is Exception:
    - An Exception is a runtime error that occures during program execution 

    - Exception interrupts the normal flow of the program 

    - Python provides a mechanishm to handle these exceptions using exception handling.


    try 
    except 
    else 
    finally 
    raise 
    assert 
    custom exception 


Basic Syntax;

    try:
        # Code Which may cause error 
    except ExceptionType:
        # Code to handle error 

    try:
    num=int(input("Enter Number"))
    result=10/num
    print(result)
    except ZeroDivisionError:
    print("Cannot divide by Zero")
    except ValueError:
    print("Invalid Error")




Common Built in Exception:

    - ZeroDivisionError
        Raised when division by zero happens

    - ValueError 
        Raise when correct type is expected byt wrong value given 

    - TypeError
        Raise when operation is applied to wrong type

    - IndexError 
        Raise when list index is out of range 

    - KeyError 
        - Raised when dictionary key is not found 

    - NameError 
        - Raised when variable is not defined 

    - FileNotFoundError 
        -Raised when file does not exists 

    - AttributeError
        - Raised when object does not have required attribute 
        - x=5
        - x.append(10)

    - ImportError/MoudleNotFoundError
        - Raised when module import fails 
        - import abcbg

    - AssertionError 
        - Raised when assert fails 
        - assert 2>5



# Multiple except Blocks 

    - A try can have multiple except block 
    
    try:
    num=int(input("Enter Number"))
    result=10/num
    print(result)
    except ZeroDivisionError:
    print("Cannot divide by Zero")
    except ValueError:
    print("Invalid Error")


    - Python checks exception from top to bottom and runs the first matching one.



# Catching Multiple Exception Togather:

    Insted of writing multiple except block

    except(ValueError,ZeroDivisionError):


# USing Exception as Object 

    except ExceptionType as e:

    - This helps us to get actual error message 

    try:
    num=int(input("Enter Number"))
    result=10/num
    print(result)
    except ZeroDivisionError as e:
    print("Error is",e)


# Genral Exception class 

    You can catch all standatrd exceptions 

    try:
        x=10/0.0
    except Exception as e:
        print("Exception Occured",e)

# Order of except Blocks matters 

    Specific exceptions should come first, genral exception should come last 
 # Wrong
    try:
        x=int("abc")
    except Exception:
        print("Some Error")
    except ValueError:
        print("value Error")

# The second block becomes unreachable 

# Correct 

    try:
        x=int("abc")
    except ValueError:
        print("value Error")
    except Exception:
        print("Some Error")

# else block in Exception Handling 

        - Else runs only when No exception occures in the try Block 
    try:
        # risky code 

    except:
        # Handle Error 

    else:

        # runs if No error 

try:
    num=int(input("Enter Number"))
    result=10/num
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid Error")
else:
    print("Result is:",result)

# Finally Block in Exception handling 

    - finally always runs whether exception occures or not 


try:
    num=int(input("Enter Number"))
    result=10/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid Error")
finally:
    print("Execution Complted.........")


# Full Structure 

    try:
        risky code 

    except SpecificError1:
        # handle 1
    except SpecificError2:
        # Handle 2
    except Exception as e:
        # Genraic handle 
    else:
        # runs if No exception 
    finally:
        # Always runs 

# When to use else

    Use else for code that should run only if try succeeds

# When to use Finally 

    Use finally for cleanup tasks:

        - closing files 
        - closing database connections 
        - closing network session 
        - releasing locks 
        - cleanup messages 

# Nested try-except 

try:
    print("Outer Try")
    try:
        num=int(input("Enter Number"))
        result=10/num
        print(result)
    except ZeroDivisionError:
        print("Inner Try: Error Division by Zero")
except ValueError:
    print("Outer try: Invalie Input")

    We can write try-except inside another try exccept 

    If user enters text, ValueError is handled by outer block.

    If user enters 0, ZeroDivisionError is handled by inner block


# Raising Exception Manually 

    We can create an exception ourselves using raise 

    - raise ExceptionType("message")

    age=-5
    if age<0:
        raise ValueError(" Age cannot be negative")

# Why raise is Used

    We raise when:

        - data is invalid 
        - business rule is violated 
        - custom validation fails 
        - we want to stop execution intentionally

    balance=500
    withd=1000
    try:
        if withd > balance:
            raise ValueError("Insufficient Balance.. Please go and Earn")
    except:
        print("Priyanka ko doutt tha")

# Re-raising an Exception 

    Sometimes we catch an exception,log something, then raise it again 

    try:
        x=10/0
    except ZeroDivisionError as e:
        print("logging Error",e)
        raise

    This prints the message and still throws the original exception 



    Intead of silently handling the error, we log it and send it upward


def read_file():
    try:
        f=open("Notes.md")
        return f.read()
    except FileNotFoundError:
        print("File not Found")
        raise

def process_data():
    data=read_file()
    print("processing Data..")
    print(data)

process_data()


Output With without Exception
-----------------------------

File not Found
processing Data.. # Problem 
None



Output with Exception 
---------------------

---------------------------------------------------------------------------
FileNotFoundError                         
FileNotFoundError: [Errno 2] No such file or directory: 'Notess.md'


Why Re- reaising is important:

Reason 1: Logging the Error 

    - Sometimes we want to log the error, but still let the program know something failed.


    try:
        x=10/0
    except ZeroDivisionError as e:
        print("logging Error",e)
        raise

    - We record the error but don't hide it 

Reason 2 - Layered architecture 

Example system layers 

APi layer 
Service layer 
Database layer 

If DB fails :

    DB layer ---> log error --> re-raise
    service layer-> catches and handle 


def database():
    try:
        x=1/0
    except ZeroDivisionError:
        print("DB error logged")
        raise
        

def service():
    try:
        database()
    except ZeroDivisionError:
        print("Service handling Error")

service()


Reason 3: Avoid hinding bugs 

Bad code:

    try:
        x=1/0
    except:
        pass

# this hides error completely 
    program contines silently 

correct approch :

    try:
        x=1/0
    except Exception:
        print("Something Faild)
        raise


Real world 
----------

Lambda --> Glue job---> redshift


def run_glue_job():
    try:
        start_glue()
    except Exception:
        logger.error("Glue job failed")
        raise

Lambda sees the error
Step funtion marks pipeline Failed 
SNS sends alert 



If we don't re raise piplene 

SUCESS 


-------

Re- raising an exception means catching an error, doing some work (like logging) and throwing the same error again so higher level code can handle it. 


# User Defined Exception:

These are custome exception created by you. instead of using built in like:

    - ValueError 
    - TypeError 
    - FIleNotFOundError 


Why do we need them?

    - Becasue buit in exception are too genreric 
    - Example - rasie ValueError("Something went wrong")


    Specific 

        - raise DataValidatationError("Invalid cutomer data")

        Logs become :
            - clear
            - readable 


How to create User Defined Exception:

    - Create a class that inherit from Exception 

    class MyError(Exception)
        pass


# assert and AssertitonError 


# Rules 

    - Keep only risky code inside try

    - Catch specific exception whenever possible 

    - Use Exception as e for debugging/logging

    - Do not silently ignore Exception unless absoulty needed 
        try:
            x=10/0

            except:
                pass 

        This is dangeous error is hidden 



    - Use finally for cleanup 

    - Do not use exception for normal control flow unless it is meaninigful 





    
# Note: Exception Handling with Constructor --- 





