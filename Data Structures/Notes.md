# Notes for Data Structures
 1. What is Data structure?
    - A data structure is a way to store, organize and access data efficiently.

    Build in Data structre Python :

*************************************************************************************************************************************
                                                    LIST
*************************************************************************************************************************************

What is List?

    - A list is a collection data types used to store multiple values in a single variable.

    Key Properties:
        - Ordered (Maintains insertition order ) : Order is preserved because list is sequence
            a= [5,1,5]
        - Mutable ( Can be changes: add/remove/update) 
        - Allow Duplicates 
        - Can hold mixed datatype (int,str,float,other list)
        - Iterable ( We can loop over it)

    Examples :

        nums=[10,20,30]
        mix=[1,"Hello",3.5,True]
        Nested= [[1,2],[3,4]]

    x=[1,"Hello,3.5,True,[2,3]]


    Indexing in LIST
    ----------------

        - Indexing means accessing a single element from list using its postiion.

        a=[10,20,30,40,50]

        index               value 
        0                   10
        1                   20
        2                   30


        a[2] = 30 

    Positive Index 
    ---------------
    print(a[0]) 
    print(a[3])

    Rule : 

        0 <= index < len(list)

    Negative Index:
    --------------

    index                   value 

    -1                      50
    -2                      40
    -3                      30
    -4                      20
    -5                      10 


    print(a[-1])


SLICING 
-------

    Slicing extracts multiple elements from list 

    Syntax:

        list[start:stop:step]

        start: Index where slicing begins 
        stop: Index where slicing ends (Not included)
        step: How many positions to jump 

    a= [10,20,30,40,50]

    print(a[1:4]) -> [20,30,40]

    a=[10,20,30,40,50,60]

        print(a[:3]) # [10,20,30]

    logs=["L1","L2","L3","L4","L5"]
    print(logs[-2:]) # ['L4'] & ['L3'] $ ['L3','L4','L5']

    a= [10,20,30,40,50]
    print(a[1:-1]) # [20,30,40,50]


    a=[1,2,3,4,5,6,7,8]
    print(a[::2]) # [3,5,7]

    a=[10,20,30,40]
    print(a[::-1]) # [40,30,20,10]


    a= [10,20,30,40,50]
    print(a[3:0:-1]) # [30,50] & [40,30,20] & [40.30,20,10]

    a= [100,200,300,400,500]
    print(a[1:-1]) # [500,400,300,200 ] & [200,300,400]

    a=[1,2,3,4,5]
    print(a[1:4:-1]) # [4,3,2] & [2,3,4] & []

Rule:

Step Negative : Start must be greater than stop 

list[start:stop:step]

start index to begin 
end   index to stop (Not Included)
steps jump size 

1. Start is included and Stop is excluded 
2. Default value 
   - a[:]  Full copy 
   - a[:3] start at 0
   - a[2:] stop =end 
   - a[::] start =0, end = len step = 1

3. step > 0 
    3.1 Traversal is left to right 
    3.2 If start > Stop -> Empty 
    3.3 If start missing -> Start = 0 
    3.4 if stop missing -> Stop = len(list)
    3.5 Steps skips element 

4. Negative Steps (step < 0)

    - Now direction changes 
        - Traversla RIGHT to LEFT 

    - When step is negative : 
       ** start must be greater than stop 
        a= [10,20,30,40,50]
        a[4:1:-1]

    4.1 If start < stop with negative step --> EMPTY 
        a[1:4:-1] -> []
    4.2 Reverse full list a[::-1]

    4.3 Default values change with negative steps 

        Expression                      Python 

        a[::-1]                        start= len(a)-1
        a[::-1]                        reverse

    4.4 Python converts negative index like :

        actual_index=len(list) + index 

        a[-1] = a[len(a)-1] 
5. Step cannot be Zero 
    a[::0] # ValueError 

6. Steps decides direction 
    potitive    left-> right 
    negative    right-left 

7. Steps applies AFTER start/stop selection 

    a[1:5:2]

    first : [20,30,40,50]

    second step : Apply step 

            [20,40]

# Updating List 

    - Updating means changing the value store at partitular index or modifying multiple values inside list. 

    nums =[10,20,30,40]
    nums[1]=200
    print(nums)

    Single Element :
        list_name[index] = new_value 

    studnets=["Priyanka","Nilam","gaurav"]
    students[1]="hello"


    marks=[50,50,70]
    marks[-1] = 100

    # Updating Multiple elements : (Slicing)

        - list[start:end] = new Values 

        nums=[1,2,3,4,5,6]
        nums[1:4] =[20,30,40]
        print(nums)


# Updating Using Loop 

    salary=[10000,20000,30000]

    for i in range(len(salary)):
        salary[i]=salary[i] * 1.10 
    print(salary)


# Udating using Condition 

marks=[90,35,60,20]

for i in range(len(marks)):
    if marks[i] < 40:
        marks[i] = 0
print(marks)


# Nested List 

List inside List 

    [3,[],[]]
a= [3,[1,2],[3,4]]

a= [3,[1,2],[3,4]]
print(a[1][0]) 
print(a[2][1]) 
print(a[0]) 

# Updating nested List 

data=[[1,2],[3,4],[5,6]]
data[1][0]= 300

First index : Outer List 
second index: Inner List 

nums=[10,20,30]
for i in range(len(nums)):
    nums[i]=2*nums[i]
print(nums)

nums=[x*2 for x in nums]


data =[
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]

]


<!-- def get_diamension(lst):
    dim=0
    while isinstance(data,list)
        dim +=1
        if len(lst)==0
            break
        lst=lst[0]
    return dim 
data[[[1,2],[3,4]]]
print(get_diamension(data)) -->


# Adding Elements to List 

    - We can add data anytime after list creation. 

        - List are mutable 
-- Ways to add eleemnts 
-------------------------

Methods             Purpose 

append()            Add single element at end. 
extend()            Add multiple elements 
insert()            Add elements at specific position 

1. append :
    - Adds One element at the end of the list.
    - Modifies the list in place 

    syntax 

    list_name.append(value)


    fruits=["apple","bananna"]
    fruits.append("mango")
    print(fruits)

    output
    ------
    ["apple","bananna","mango"]

Internal Working : Python simply increases list size and places element at last. 
(Dynemically Grows in size)

Important Concept
-----------------

append() adds the whole object, not individual items 


a=[1,2]
a.append([3,4])

print(a) # [[1,2],[3,4]]


2. Extend() - Add Multiple elements 

    - Add multiple elements from iterable
    - Flattens the added items 
    - Used when merging the lists 

    syntax 

    list_name.extend(itrable)

        a=[1,2]
    a.extend([3,4])

    print(a) # [1,2,3,4] # Faltten 

    Diffrence from append()
    ------------------------

    a=[1,2]
a.append([3,4])

print(a) # [[1,2],[3,4]] # Nested list 


3. Insert() - Add at specific position 

    - Adds elelemnts at a given index 

    list_name.insert(index,value)

    name=["Hello","Hi","Priyanka","Nilam"]
    names.insert(1,"Gaurav")

    - Python shifts all ements to the right : So performnace is not good 


4. Using + operator 
--------------------

    Creates a new list by combining lits 

    list 3= list1+ list 2 

    a= [1,2]
    b= [3,4]

    c=a+b 
    print(c)

    [1,2,3,4]


5. Using List concatenation with += 
------------------------------------
a= [1,2]
a += [3,4]

print(a)

[1,2,3,4]

------------------------------------------------------------------------------------------------------------------------------------

6. Addig Elements using Loop 

result=[]

for i in range(5):
    result.append(i*10)
print(result)



matrix=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(i*j)
    matrix.append(row)
print(matrix)



nums=[1,2,3]
for i in range(3):
    nums.insert(0,i)
print(nums)


Comparision 
------------

Method      Adds                 Position            Performance 

append      single element        end                 fast
extend      multiple element      end                 fast
insert      single element        anywhere            slow


Removing Element Methods :

    - remove() -> remove by value 
    - pop() -> remove by index 
    - clear() -> remove all element 

remove()   : Deletes the first occuurrence of a value from a list.

            list.remove(value) 
                - Modifies original list
                - Return None 

nums=[10,20,30,40]
nums.remove(20) 

[10,30,40]

        ValueError : if X is not present in list 

if 5 in a:
    a.remove(5)

records=["Priyanka","Nilam","Unknown","Amit"]

nums=[1,2,2,3,2]

while 2 in nums:
    nums.remove(2)
print(nums)

[1,3]


Pop() : Removes element using index - Also Returns removed element 

    list.pop(index)

    By default: list.pop() -> Removes last element

    nums=[10,20,30]
    x=nums.pop() # By default
    print(x)
    print(nums)

clear() : Deletes eveything (Element) from list 

list.clear() 

Note: Memory stays allocated but elements removed. 

------------------------------------------------------------------------------------------------------------------------------------

records=["Priyanka","Nilam","NULL","Amit","NULL","NULL",HELLO","NULL"]

while "NULL" in records:
    records.remove("NULL")



status=["SUCESS","FAILED","SUCCESS","FAILED"]

# Remove one failed record maunually 

status.remove("FAILED")


files=["data.csv","temp.log","report.csv","debug.log"]

for f in files [:]:
    if ".log" in f:
        files.remove(f)
print(files)


# messages="msg1","msg2","msg3"

messages=["msg1","msg2","msg3"]

latest=messages.pop()
print("Processing:",lastest)


records=["Priyanka","Error","Nilam","Error","Amit","Error","Gaurav","Error"]    

# Step 1 - Remove invalid 

while "Error" in records:
    records.remove("Error")

# Step 2 - Process One by one 
proccessed=[]
while records:
    processed.append(records.pop())

print(processed)

processed.clear() 
# 

--- Searchig Methods 
---------------------

    1. index() - > Find POSITION of value 
    2. count() -> Count occurrence 

index() : Returns the index (Position) of the first occurrence of a value.

    list.index(value)

    Rules: 
        - Starts search from left 
        - Return integer index 
        - Error if value not found 

names=["Priyanka","Rahul","Nilam"]
print(names.index("Rahul"))

a=[1,2,3]
a.index(5) # ValueError : 5 is not in list 


IMP ** : Start & End range search 

list.index(value,start,end)

nums=[10,20,30,20,40]
print(nums.index(20,2)) # Start searching 


Count() : Counts how many times value appers 

list.count(value)

nums=[1,2,3,2,3,2]
print(nums.count(2)) # 3

status=["Sucess","failed","sucess",failed"]

if status.count("Failed") > 0:
    print(" Some records failed")


Advance: 

data=[1,1,2,3,3,3] 

Output:

1   2
2   1
3   3 


a=[1,2,3,2]
a.remove(2)
print(a.count(2)) # 1

a=[10,20,30]
print(a.pop())
print(a.index(20)) # 1





---- Ordering Methods 

sort(): Arrenges elements ascending by default 
    list.sort()

    - Modify original list 
    - Return None 
    nums=[5,2,8,1]
    nums.sort()
    print(nums)

Descending Order:

nums.sort(reverse=True)
        
data=["apple","kiwi","banana"]
data.sort(key=len,reverse=True)

reverse() : Reverse current order of list 

nums=[1,2,3]
nums.reverse() #3,2,1

3,2,1 => 1,2,3

-------------------------------------------------------------------------------------------------------------------------------------
a=[10,20,30]
    - Python creates a list somewhere in memeory
    - Variable a only stores the address of that list.

Assignment operator:

a=[1,2,3]
b=a

a   ---------
            ----->[1,2,3]
b   ---------


Note: Noth Points to Same Memory location.


If we try to modify b :

b.append(4)


Sahllow COPY (Real Copy ):
--------------------------
a=[1,2,3]
b=a.copy() 

It will create 2 sepearte object with diffrent memeory location.

a=[[1,2],[3,4]]
b=a.copy()

b[0][1].append(99)

Shallow copy creates a new container/address but copies only refrences of nested objects, Not 
the objects themselves. Therefore mutations inside nested mutable objects affects both original and copied structure.

Trap : Questions 
----------------
1. 
a=[1,2,3]
b=a
b.append(4)
print(a) #[1,2,3,4]

------> b=a is not copy -> Both points to same memeory 


2. 
a=[1,2,3]
b=a.copy()
b[0]=100
print(a) # [1,2,3]

3. Nested List 

a=[[1,2],[3,4]]
b=a.copy()
b[0][0]=100
print(a) # [[100,2],[3,4]]

--> Inner list share same memory 

    -> Shallow copy copies only outer list 

4. a=[[1],[2]]

    b=a.copy()
    b[0].append(99)
    print(a) # [[1,99],[2]]

    # Both points the same inner 


5. a=[[1,2],[3,4]]
   b=a[:]
   b[0][0]=100
   print(a) # [[100,2],[3,4]]


    Important Interview :

Rule 1 : Shallow copy :
        - New container 
        - Same elements 

Rule 2: If elements are mutable --> Change and reflect 

Rule 3 : If elements immutable --> appears indepenednt 

"Shallow copy duplicates only first level container, while nested object remain shared through reference copying"


Deep Copy:
------------

    - Deep copy creates compltely independent clone of an object. 

        - New outer list 
        - new inner list 
        - New nested object

       ** Nothing is shared 

    import copy 
    a=[[1,2],[3,4]]
    b=copy.deepcopy(a)

1. 
    import copy 
    a=[[1,2],[3,4]]
    b=a
    c=copy.deepcopy(a)
    b[0][0] =100
    print(a) #[[100,2],[3,4]]
    print(c) # 

b=a => Same Momory 
deepycopy() -> New memeory 

2. 
import copy
a=[10,20,30]
b=copy.deepcopy(a)

print(id(a[0]))
print(id(b[0]))

# Integer are immutable 
Deep copy does not recreate immutbale objects - Python Resuses them 


Methods                Copy Type 

=                       No copy 
copy()                  Shallow 
[:]                     Shallow 
deepcopy()              Deep 


Built In Functions 
-----------------

1. len() : Return number of elements 

a= [10,20,30] 
len(a) #3 

2. min() and max() 
Samllest/larget value 
min(a)
max(b)

3.sum() # Addes numeric values 

    a=[1,2,3]
    sum(a)

4. sorted() 
    - Returns new sorted list ( does not change original)
    - a=[3,1,2]
    b=sorted(a)

Difrrence from sort and sorted() 

sort()                           sorted() 
- modifies list                 - creates new list 

5. reversed() 
    - Return reverse iterator 

6. any() 

    - Return True if at least one element is true.

    False values : 0,0.0,"",[],{},None,False 

    print(any[0,0,5,0]) # True 
    print([]) # False 

    status=["OK","OK","ERROR"]

    print(any(s=="ERROR" for s in status))

7. all()

    Return True if all elements are true. 

    print(all[1,2,3]) # True
    print(all([1,0,3])) # False 

8. enumerate() : 

    - Enumurate() gives you number + value togather while looping 
    - Without enumurate you only get values 

    (index,value)

    for name in names:
        print(name)


Q. arr=[5,7,9,7] # 7 

for i, x in enumurate(arr):


i=0
for x in names:
    print(i,name)
    i +=1 
-----------------------------------------------------------------------------------------------------------------------------

zip() : Zip() is a built in python used to combine multiple iterables(lists,tuple,string) element by element. 

It joins items from each iterable based on their same postion(index)

Syntax:

    zip(iterable1,itrable2,itrable3.............)

What does Zip return?

zip() returns a : zip object Not a List 

a=[1,2,3]
b=[20,30,40]
z=zip(a,b)
print(z) # <it returns zip Object> [TO see the values we need to use list()]


print(list(z)) # [(1,20),(2,30),(3,40)]


zip() : Shortest list decides the lenght 


zip_longest() is a function from itertools module 

it works like zip() but Instead of stopping at shortest iterable It continues untill the longest iterables ends.

Syntax:

import itertools import zip_longest

zip_longest(itrable1,itrable2.......)


Parameters :

itrables : list/tuple/strings 

fillvalue : value used when element are missing 

default fillvalue  : None 
-----------------------------------------------------------------------------------------------------------------------------------

list() -> convert itrables to list 

    - Is a built in function that converts any itrable into list.

    Itrable Means : 
        - string 
        - tuple
        - set
        - dictionary
        - range 
        - zip object 
        - map/filter object 
        - genrator 


reveresd() -> reverse itrator 
------------------------------
    - Returns items in reverse order without changing original list 
    -  Returns Object 
    - To see the output we need to convert it to list using list() 

    Reversed                                reverse 
    return itartor                          modify list 
    original unchanged                      original changed 



map() - 
    a=[1,2,3,4,5]

    for i in a:
        print(i*i)
    - Applies a function to every element of iterable.

    - map(function,itrable )

    - Return map object 
    - Lazy Evalution 

    
    map() needs functions:

        - Create function using def.
        - create function instantly using lambda

    def multiply(x)
        return x*2

    nums=[1,2,3]

    result=list(map(multiply,nums))
    print(result)


    lambda: Temporary function


    internal :
    result=[]
    for item iterbale:
        result.append(function(item))


    a=[1,2,3]
    b=[4,5,6] # output [5,7,9]

    result=list(map(lambda x,y:x+y,a,b))



filter() - select elements based on a condition 
    - It keeps only items where condition= True

    syntax :

        filter(function,iterable)

        True:- Keep elements 
        False- Discard elements 

    result=[]
    for item in iterable:
        if function(item):
            result.append(item)


nums=[1,2,3,4,5,6]
even=list(filter(lambda x: x%2==0,nums))
print(even)

map() vs filter() 

map                           filter 
Transform data                select data
modified element              Subset return
Any value                     True/False
x*2                           x%2==0

########################################.  TUPLE . #################################################################################

What is Tuple?

    - A tuple in python is an ordered,immutable collection of elements.
        - Ordered 
        - Indexed 
        - Immutable 
        - Allow duplicates 
        - Faster than List 
        - Hashbale (dict keys/sets)

    cols=("country","city","date")

    t=(10,20,50)


Creating Tuple
-------------

    - Using Parenthesis 
        t=(1,2,3)

    - without parenthsis 
        t=1,2,3

        Note: Comma makes tuple, not bracket

Single Element Tuple
-------------------

t=(5,) # Tuple (comma is imp)

t=(5) # Int 


Using tuple:
----------

    - tuple([1,2,3,4])
    - tuple("abc")

Nested tuple 

t=((1,2),(2,3),(4,5))

t=(1,(2,3),(4,5))


Tuple Packing and Unpacking 
---------------------------

packing
t=10,20,30 #t=(10,20,30)

unpacking
a,b,c=t


a,_,c=1,2,3 # tuple 

# Python will unpack each value one by one into variables on the left.

value assign 

a   1
_   2
c   3 

Why _ is used?

    _ is a conversion in python :
        " I dont't care about this value"

# It's not special syntax - it's just a variable name that developers use to ignore values.

def process():
    return True,"DATA","LOSS"

status,_,logs=process() 

# but you only need first and last value we ignored middle value 

a,_,_,d=(1,2,3,4)

# For Loop 

pair=[(1,10),(2,20),(3,30)]

for _,value in pair:
    print(value)


Extended Unpacking 
------------------
This is called extended iterable unpacking 
# It allows one variable to capture multiple remaining values 

a,*b=(1,2,3,4,5) 

a   1
b   [2,3,4,5] # b becomes a list not tuple 


Example:
_,*rest(10,20,30,40,50)



# Tupe Indexing 

Tuple indexing means accessing elements of a tuple using their position (index number )

     - index always start from 0

t=("apple","banana","mango")

print(t[0]) # apple 
print(t[1]) # banana 


Negative Indexing 
----------------

print(t[-1]) # mango 
print(t[-2]) # banana 


Indexing Nested Tuple 
--------------------

t=(1,(2,3),4)
print(t[1]) #(2,3)
print(t[1][0]) # 2 

Tuple Indexing in loop 
----------------------

t=("A","B","C")
for i range(len(t)):
    print(i,t[i]) 

output 
------

0   A
1   B
2   C

# Indexing With Slice 

t=(10,20,30,40,50)

print(t[1:4]) # (20,30,40)


# Cannot Modify Using Index 

    - Tuple are immutable 


t=(1,2,3)

t[0]=100

# TypeError: 'tuple' object does not support item assignment

Indexing 

sliciing 

Tupe vs List 

    - Same Syntax 
    - Same behvaiour 
    - But tuple result is immutable 



 t=(10,20,30,40,50,60,70)   

 print(t[::3]) #(10,40,70)

 print(t[1:6][: : -1]) # 20,30,40,50,60 -> 60,50,40,30,20

 print([-3:]) #50,60,70

 print(t[1:-1]) # Drop First & Last element 

 mid=len(t)/2 7/2 =3.5 => 3

 left=t[:mid] # (10,20,30)
 right=t[mid:] #(40,50,60,70)


 PART-2 : Slice + Unpacking 

 t=(10,20,30,40,50,60,70)  

 first,*rest=t

 first=10
 rest=[20,30,40,50,60,70]

 a,*middle,b=t


 a=10
 middle=[20,30,40,50,60]
 b=70

 a,b=t[:2]
 a=10
 b=20

 _,_,*remaining=t

 reamining =[30,40,50,60,70]


 row=("ID101","2026-02-28","Pune","India", 5000,"Active")

    - user_id
    - location feilds 
    - status 
    - salary 

user_id,*location,salary,status=row


Nested Slice + Unpack 
---------------------

data=(1,2,3,4,5,6,7,8)

left_half=data[:4]
a,*mid=left_half

print(a)
print(mid)


    Tuple immutable - 
        Below methods are not used in tuple:

         append() 
         remove()
         pop()
         extend()
         sort() 

    Tuple methods:
        count() 
        index() 

1. tuple.count(value) 

    Count how many time a value appers inside tuple 

tuple.count(5) 

t=(1,2,3,2,4,5)
t.count(2) #2

Working with string inside tuple

NOTE:
    t=(1,2,3)
    print(t.count(4)) # 0

# No Error - just return 0


tuple.index() 

# tuple.index(value,start,stop)
    - value : Required 
    - start - Optional
    - end - Optional


    Return the first occurance index of value.

    t=(10,20,30,40)

    print(t.index(30)) # 2

    t=(1,2,2,3,4)
    print(t.index(2)) # 1 

    t=(1,2,2,3)
    print(t.index(2,2)) # 2

NOTE:
    t=(1,2,3)
    print(t.index(5)) 

    # ValueError - x not in tuple 



Q. WHy tuple has fewer methods then list?

    - BEcause tuple is immutable and does not support modification operation.



Built- in Function :

    1. len() # Return numbers of elements       # count elements 
    2. min() # Return smallest element          # Samllest 
    3. max() # Return largest element           # largest 
    4. sum() # Adds numeric values # Total 
    5. sorted() #Returns sorted resukt as list, NOT TUPLE       # sorted list 
    6. any() # Return TRUE if at least one value is True        # at lest one true
    7. all() # Return True if all values are True               # all true
    8. enumurate() # Return index + value pairs                 # index+value
    9. zip() # Combine multiple tuples                          # combine iterables 
    10.tuple() # Convert iterable to tuple # print(tuple([1,2,3]))  # convert to tuple 
    11. reversed() # Return reverse iterator                        # reverse iterable 
    12. list() # Convert tuple to list # t=(1,2,3) # [1,2,3]        # convert to list
    13. set() # Convert tuple to set() #t=(1,2,3) print(set(t))     # Remove duplicate 
    14. sorted() with key                                           # 

        t=(("A",3),("B",1),("C",2))
        print(sorted(t,key=lambda x:x[1])) # 

    15. hash() # Tuple is hashable if element are hashable          # hashing 


################################################## SET ############################################################################

What is set in python?

    - A set is :
        - An unordered collection of element 
        - A collection of unique values 
        - A mutable data structure 
        - Written using {} curly braces 


    unordered = No Index position 
    No duplicates = Unique values 
    Mutable = Can add/remove/update
    No indexing = Cannot access via index 
    Fast lookup = Very effieient memebership checking 


    Creating a Set
    -------------

    1. Curly braces 

        s={10,20,30}

    2. set() constructor 

        s=set([1,2,3,4,5])

    3. Empty set 

        s={}
        print(type(s)) # dict 

        s= set() 


    Duplicate Removal :

    nums={1,2,2,3,4,4}


    Accessing Element in set:
    -----------------------

    for item in s:
    print(item)


    Adding elelemts:
    ---------------

    add() 
    - Add single element 
    - If element already exists -> Nothing 
    - Set unique 

    s={1,2}

    s.add(3) 

    update() 
    - Add multiple elelemnts 
    - Accept list,tuple,set 
    - Remove duplicate automatically 


    s={1,2}
    s.update([3,4,5])
    print(s)

    # You can pass - list,tuple,set 


    Removing elelemnts 
    -----------------

    remove(value) 

    s.remove(2) # Error if element not present 


    discard(value ) 

    s.discard(100) # No error if not present 


    pop() 
    - Removes random element 
    - Because set is unordered
    - returns removed element 


    s.pop() 

    clear() # Remove all elements 

    s.clear() 


copy() 
------

copy() is used to create duplicate (shallow copy) of set 

It creates a new set object with same elements as the original set 

new_set=orginal_set.copy()

s1={1,2,3,4}
s2=s1.copy()

Note:
        copy() creates a new set in memory 

    so changes in one set do not affect the other. 

    s1={1,2,3}
    s2=s1.copy()
    s2.add(4)

    print(s1) # {1,2,3}
    print(s2) # {1,2,3,4}



s1={1,2,3}
s2=s1

s2.add(4) # 

# Becasue both variable point to same object 


Mathematical Set Operations 
---------------------------

- Union()

    - Combine sets 
    - set1.union(set2)

    A={1,2,3}
    B={3,4,5}

    print(A.union(B)) # {1,2,3,4,5}

    A|B - Union (Shortcut)


- intersection() 
    - Common elements 
    - A. intersection(B)
    A={1,2,3}
    B={3,4,5}
print(A.intersection(B)) # {3}

A & B - Intersection (Shortcut)


- symmetric_diffrence()

    Elements in wither set but not both
    print(A.symmetric_diffrence(B))

    A={1,2,3}
    B={2,3,4}

    {1,4}

    A ^ B - symmetric_diffrence (Shortcut)


- intersection_update() 

    Updates original set 
    A.intersection_update(B)

    A={1,2,3}
    B={2,3,4}

    output: {2,3}

    meaning: set1.intersection_update(set2)

            - Update set1 so that it only contains elements that are present in both set1 and set2 

- diffrence_update() 

    - update original set 

    A={1,2,3}
    B={2,3}

    Output: {1}

- symmetric_diffrence_update()

    - update original set 

      A={1,2,3}
      B={3,4}

      output: {1,2,4}


Set Relationship methods
------------------------

subset          Samll set inside big set 

superset        Big set containing small set 


- issubset()
    - Check it set is subset

    A={1,2}
    B={1,2,3}

    print(A.issubset(B)) #True

- issupersubset()

    A={1,2,3}
    B={1,2}

    print(A.issuperset(B)) # True


- isdisjoint() 

    - Checks if sets have no common elelemnts 

    A={1,2}
    B={3,4}

    # True 

sepecial Case:

    - Every set is a subset of itself. 

    A={1,2,3}

    print(A.issunset(A)) # True 



Built-in functions 
-----------------

len() # Return number of elements 
min() # Samllest value
max() # Largest value
sum() # Add numbers
sorted() # sorted list 
any() # Returns True if any element is True
all() # True if all elements are True




#########################################Dictionary##################################################

What is Dictionary?

    Python used to store data in key-value.

    - It is used when you want to connect one piece of data with another.

    students =["Priyanka",30,4000,"pune"]

    students={
        "name":"priyanka",
        "age":30,
        "salary":4000,
        "City":"pune"
    }

    key:value 


- Why do we use dictionary:

    - data has a label/name
    - fast lookup is needed 
    - Data is not suitable for index- based access 
    - We want meaningfull access instead of numeric index 

Fetaures:

    - stores data in key-value pair 
    - is mutable -> Can change after creation 
    - Is unordered conceptually for loopup, but in python 3.7+ inseration order is preserved 
    - Keys must be unique 
    - Key must be immutable/hashable 
    - Values can be of any data type 
    - allows mixed data type 
    - nestsed dictionaries are possible 


Rules:

1.  Keys must be Unique:

    d={"a":10,"a":20} ---> {"a":20} Latest value 

    # The latest value overwrites the old one 

2.  Keys must be immutable 

    Allowed Keys:

        - string 
        - int 
        - float 
        - tuple (if tuble contains immutable items)
        - bool 

    Not allowed:

        - List 
        - set 
        - dictionary 

3.  Values can be anything 

    d={
        "name":"Priyanka",
        "age":30,
        "Marks":[80,89,70],
        "address":{"city":"Pune","stste":"MH"}
    }

- How dictionary works internally :

    Dictionary works using hashing 

        - When you give a key :

            - Python computes a hash value
            - Uses that hash to find where data is stored 
            - gives value quickly 

        Note: That is why dictionary lookup is usually very fast 


        d={"Name":"abc"}

        d["Name"] -'abc'

        # Note: Python does not search one by one like list it directly goes to the location using hash of "name"

        That is why, dictionaries are effieicent.


Creating dictionaries 
---------------------

1. Using curly braces 

    students={
        "name":"priyanka",
        "age":30,
        "salary":4000,
        "City":"pune"
    }

print(students)


2. Empty Dictionary

d={}

print(d)

3. Using dict() constructor 

    d=dict(name="Hello",age=25)

4. From list of tuples 

    d= dict([("name","Hello"),("age",25)])

5. Using Zip() 

    keys=["name","age","course"]
    values=["Priyanka",25,"Python"]

    d=dict(zip(keys,values))

    print(d)

6. Using fromkeys() 

    # fromkeys - Method used to create a new dictionary using a list (or any iterables ) of keys with the same value for all keys.

    keys=["a","b","c","d"]
    d=dict.fromkeys(keys,0)
    print(d)

    {'a':0,'b':0,'c':0}

    Example 1: 

    keys=["a","b","c","d","e"]
    d=dict.fromkeys(keys,0)
    print(d)


    Example 2:

    keys=["a","b","c","d","e"]
    d=dict.fromkeys(keys)
    print(d)

    Default value : None 


    Example 3 

    keys=["id","name","age"]
    d=dict.fromkeys(keys,[])
    d["id"].append(1)
    print(d)

    {'id': [1], 'name': [1], 'age': [1]}

     keys=["id","name","age"]
     d={k:[] for k in keys}
     d["id"].append(1)
     print(d)

    # Because all keys points to same list object in memeory. 


- Access values in dictionaries 
--------------------------------

    - Using key with square bracket 

        students={"name":"hello","age":25}

        print(students["name"])

        # If key does not exists : KeyError 

    - using get()
        students={"name":"hello","age":25}
        print(students.get("name")) # Hello
        print(students.get("Course")) # None # No error 

        # You can also set default value:

         print(students.get("Course","Not Found")) # Not Found


Adding and Updating elements:
----------------------------

    - Add new key-value pair 

        students={"name":"hello","age":25}

        student["course"]="Python"
        print(students)

    - Update existing value 

        students={"name":"hello","age":25}

        students["age"]=26

        print(age)

    - Add multiple values using update() 

        - student.update({"city":"pune","state""MH"})
        print(students)


- Diffrence between add and update in dictionary 

    d["new_key"]=value # add 

    d.update({.........}) 

    Note: Dictionary has no seprate add() method 

- Removing elements from dictionary 

    - pop() 
        - Removes key and return its value 

         students={"name":"hello","age":25}
         x=students.pop("age")
         print(x)
         print(students)

         If key is missing " KeyError 

        students={"name":"hello","age":25}
        x=students.pop("course","Not Found")
        print(x)



    - popitem() 
        - Remove and return the last inserted key-value pair 

        d={"a":1,"b":2,"c":3}
        print(d.popitem()) # {"c":3}
        print(d)

    - del

        d={"a":1,"b":2}
        del d["a"]
        print(d)

    - clear()
        d={"a":1,"b":2}
        d.clear()
        print(d)


Dictionary Methods :

    clear()
        - Removes all items from dictionary 
        Use cases:
            - reset setting 
            - empty 
            
    copy()
        - Return a shallow copy of dictionary
        d={"a":1,"b":2}
        d2=d1.copy()
        print(d2)
        Shallow copy - 
            Outer Dictionary : New Object 
            Inner Object : Same Memory refrence

        Deep Copy :
            Completly independent copy 
            import copy
            copy.deepcopy()


    fromkeys()
        - creates new dictionary from given keys with same value 
        - keys["name","age","city"]
        - d=dict.fromkeys(keys,None)
          print(d)


    get() 
        - Returns value of given key, If key not found returns default 
        use cases:
            - Avoid KeyError 
            - API 

    items()
        - Returns view object containing key-value pairs as tuple 
        - d={"name":"Hello","age":30}
        - print(d.items) # dict_items([('name', 'Hello'), ('age', 30)])
        - returns dict_items 
        - Each element is a tuple 
        - (key,value)

    keys()
        - Keys() returns all the keys of the dictionary
        - It returns a special object called dict_keys
        - This is Not a list but view object 

    values()
        - Returns all the values of the dictionary
        - dict_values 
        

    Methods         Returns             Output Type             Usecase 
    Keys()          All Keys            dict_keys               iterable keys
    values()        All values          dict_values             Itreable Values 
    items()         key-value pair      dict_items              iterable dictionary 


    pop() 
        - removes specified key and return value 
        - print(d.pop("a"))

    popitems()
        - Removes last inserted item and return tuple

    setdefault()
        - Returns value of key if key exists if not exists, insert key with default value

    update()
        - Updates dictionary with another dictionary or iterable key -values pairs 
        - d={"a":1,"b":2}
        - d.update({"b":20,"c":30})
        - print(d)

Dictionaries Operator:

    in 
        - Checks key existsence 
        - d= {'name': 'Hello', 'age': 25}
        - print("name" in d)
        - print("age" in d)
    not in 

- Assignment operator 

    = d["age"]=40

- Merge operator
    d1={"a":1,"b":2}
    d2={"b":20,"c":30}

    d3=d1|d2
    print(d3)

    {"a":1,"b":20,"c":30}


Built Functions :

    - len()
    - type() # Returns type object 
    - str() # Converts dictionary to string ************
    - dict() # Creates dictionary 
    - sorted() # Returns sorted list of keys 
    - min() # Returns min key
    - max() # Returns max key
    - sum() # Works on numeric keys or numeric values 
    - any() # Returns True if at least one element is true
    - all() # Returns True if all elements are true
    - list() # convert keys into list by default 
    - tuple() # 
    - set() 
    - revered() # Wroks on dictionary keys in reverse insertion order
    - enumurate() # Loop 

Dictionary Comprehension :
-------------------------

Used to create dictionary in one line 

syntax:

    {key_expr:value_expr for item in iterable}


nums=[1,2,3,4]
square={x:x*x for x in nums if x%2==0}
print(square)



Dictionary VS LIST 

storage 
access
Example 
order 
Meaning lables 
Loopkup speed 

DIctionary VS Tuple 

storage 
access
Example 
order 
Meaning lables 
Loopkup speed 

Dictionary VS Set

storage 
access
Example 
order 
Meaning lables 
Loopkup speed 


############################################## STRING ###############################################################

What is String?

    - A string is a sequence of characters enclosed in quotes.

        - letters 
        - numbers 
        - symbols 
        - space 

    - name="Priyanka"
    - city="Pune"
    - senetance= " Priyanka Living in pune"
    - number="1234"

Imporatant Points:

    - String is Immutable 
        - Once created it cannot be changed 
    - Strings are ordered 
    - Strings are itrable


Ways to create String:

1. single quote 

    a='Hello'

2. Double quotes 

    b="hello"

3. Triple Quotes ( Multi line)

    text=""" this is multi line 
        stings"""


String Indexing :

Every charcter has a position called index.

text="PYTHON"

P   Y   T   H   O   n
0   1   2   3   4   5

-6  -5  -4  -3  -2  -1


Access Charaters:

print(text[0])

print(text[-1])

String Slicing 
--------------

Extract multiple chacters :

string [start:end:step]

END : Excluded 

String Lenght:

-- print(len(text))

-- String Concatenation 

-- String Repetition 

-- Membership Operator:

 text="python"
 print("p" in text) # True


-- Iterating String 

    text="python"

    for ch in text:
        print(ch)


String FUnction :

upper() 
    - Convert to uppercase 

lower() 
        - convert lowercase 

title()

    - First letter of each word capitalized
    - text="data engineering course"
    - print(text.title) #


capitalize() 

    - First letter capitalized

swapcase() 

    - Upper -> Lower 
    - Lower -> Upper 

casefold() 

    - stronger lowercase ( used for comparision)


2. Alingment & Formatting :

center() 
    - center the string 
ljust()
    - left align 

rjust()
    - right align 

zfill()
    - Fill with zeros on left 
    - print("42".zfill(5)) # 00042

Searching Methods :
--------------------
find() 
    - Used to find chacters or substrings 
    - text="python"
    - print(text.find("t")) # 2
    - Returns Index 
    - Returns -1 if not found

rfind() 
   - Search from right side 

index() 
     - Same as find but throw error if not found 

rindex() 
    - Search from right 


Counting :
--------

count() 
    - Count occurance 

Checking/validation 
-------------------
    -  returns True / False 
    


format()
    - Used to insert values inside string 

    - string.format(value1,value2)
    
    name="Nilam"
    age=30
    print("My Name is {} and age is {}.format(name,age))

    {} -> Acts as a placeholder wheres values will be inserted

    print("My Name is {0} and age is {1}.format("Nilam","30"))

format_map()
    - Same as formte() but works with dictionary 
    - string.format_map(dictionary)
    - data={"name":"Nilam","age":30}
    - print("My name is {name} and age is {age}.format_map(data))

index() 

    - Returns position of substring 
    - string.index(substring)

    - text="python"
    - print(text.index("t")) # 2

    - If not found --> Error (valueError)



isalnum() - Checks if strinfg contains letters or numbers only (True/False)
          - print("Python123".isalnum()) 

isalpha() - Checks if string contains letters only
          - print("Python".isalpha()) # True

isascii() - Checks if charcters belongs to ASCII range (0-127)
          - print("Python".isascii()) # True

isdecimal() - Checks decinmal numbers only 

isdigit() - Checks digits 

isnumeric() - Checks numeric characters 

isidentifier() - Checks if string is valid variable name 

islower() - Checks if all letters are lowercase 

isprintable() - Checks if string contains printable chacaters 
isspace() - Checks if string contains only spaces 
          - print("  ".isspace()) # True
         
istitle() - Checks if string is titile case 
isupper() - Upper case 


join()
    - Joins list into strings 
    - seprator.join(itrable)
    - words=["Python","Spark","Aws"]
    - print(" ".join(words))

ljust()- Left alingn string 
       - print("Python".ljust(10)) # sapaces added to right 

lower() - converrts lower case 

lstrip() - Removes spaces from left side 
         - text="     Python"
         - print(text.lstrip())

maketrans() - Creates translation table (dictionary) that maps chacters to new chacters 
            - str.maketrans(old_char,new_chars)
            - old_char: chacters to replace 
            - new_chars: chacteers to replace with 


partition() - Splits string into 3 parts 
            - string.partition(seperator)
            - text="hello world"
            - print(text.partition(" "))

replace() - Replace substring 
          - text="I like Java"
          - print(text.replace("java","Python"))

removeprefix() - Remove starting substring
               - text="unhappy"
               - print(text.removeprefix("un"))
removesuffix() - Remove Ending sunstring 
               - text="data.csv"
               - print(text.removesuffix(".csv"))
rfind() - Find substring from right 
rindex() - Same as rfind but error if not found 
rjust() - Right align String 
rpartition() - Split from right side 
rsplit() Split from right side 
rstrip()

split()
    - Used to break a string into a list of substrings using separator 
    - string --> List 
    - string.split(sepeartor,maxsplit)
    - seprator: Chacters used to split 
    - maxsplit: number of split 
    - Default sperator :Space




splitlines()
        - Splits string based on line breaks 
        - useful for reaading multi line text or files 
        - text="Hello\nWord\nPython"
        - print(text.splitlines())
        - Usecase: Processing log files 

startswith() 
        - string.endswith(suffix,start,end)
        - Checks if string begins with given substring 
        - True/False 
        - text="Python programming"
        - print(text.startswith("python"))

        - file="data_2024.csv"
        - if file.startswith("data"):
                print("valid file")

endswith() : Chesk whether a strinf ends with specific substring 

        - True : If string ends with the given value 
        - string.endswith(suffix,start,end) # start and end end option 
        - text="data.csv"
        - print(file.endswith((".csv",".json",".txt")))


strip() : Removes chacters from both the left and right side of string 
        - By default space 
        
        - NOTE: It does not remove chacters inside the string 

        - stting.strip(chacters)

        - IF no parameter passed -> removes whitespaces 

        - text="     Python     "
        - print(text.strip())

        Note: Strip() Removes all combinations of given chacters from both ends 

lstrip()

rstrip() 


translate() : Used to replace or remove chacters in a string using translation table.

            - str.maketrans() - Create a rule 
            - translate - apply rule 

            - string.translate(table)

            table=str.maketrans("ae","12")
            {
                "a":"1",
                "e":"2"
            }
            print("apple".translate(table))



education 

table=str.maketrans("aeiou","12345")
print("education".translate(table))











    






        












































































    


    

























------
pass 

























































































































# Slice create new LIST 

b=a[1:4]

Pyhton:
    - Creates New list object 
    - Copies refrences 



a=[1,2,3]
b=a 

a ---------
            ---- [1,2,3]
b ---------

Both Points to same memory 

# Python variables do not store values directly 
    - They store refrences (address) to object in memory.

# Do we copy the refrences or create a new object 


# 2 types of Copy :

    1. Refrences assignment (Not a real copy)
    2. Shallow Copy 
    3. Deep Copy 

# Shallow Copy :

    - New outer container But inner objects are shared

    a=[1,2,3]
    b=a[:]
    b=list(a)


shallow copy : Photocopy of file list but files inside same 

deep copy : Duplicate entire folder with files 








