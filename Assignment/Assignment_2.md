# Assignment 2

    1.	Given t = (10, 20, 30, 40, 50), print all elements at odd indexes using a loop.
	2.	Given t = (1, 2, 3, 4, 5, 6), count how many elements are even using a loop.
	3.	Given t = (5, 12, 7, 12, 9, 12), find the frequency of 12 without using count().
	4.	Reverse a tuple using slicing and also using a loop (two methods).
	5.	Given t = (1, 2, 3, 4), create a new tuple where each value is squared.
	6.	Given t = (10, 20, 30), create (10, 10, 20, 20, 30, 30) using a loop.
	7.	Given t = (2, 4, 6, 8), check if all numbers are divisible by 2 using if inside loop.
	8.	Given t = (3, 5, 7, 9), check if any element is divisible by 3.
	9.	Given t = (1, 2, 3, 2, 2, 4), remove all 2s (create a new tuple).
	10.	Given t = ("a", "b", "c"), build "a-b-c" using loop (no join).
	11.	Given t = (1,) and t2 = (1), explain by code which is tuple and why.
	12.	Given t = (10, 20, 30, 40, 50), print from index 1 to 3 using slicing and loop.
	13.	Given t = (10, 20, 30, 40), rotate left by 1 → (20, 30, 40, 10).
	14.	Rotate right by 2 for t = (1,2,3,4,5) → (4,5,1,2,3).
	15.	Given t = (1, 2, 3, 4, 5), split into two tuples of equal size (or near).
	16.	Given nested tuple t = ((1,2), (3,4), (5,6)), sum all numbers using loops.
	17.	Given t = (("a", 1), ("b", 2), ("c", 3)), create tuple of only keys.
	18.	Same tuple above, create tuple of only values.
	19.	Given t = ((1,2,3), (4,5), (6,)), find the max length inner tuple.
	20.	Given t = (1, 3, 5, 7), insert 4 in correct place to keep it sorted.
	21.	Given t = (5, 2, 8, 1), find second largest without sorting.
	22.	Find second smallest without sorting.
	23.	Given t = (1, 2, 3, 4, 5), compute product of elements using loop.
	24.	Given t = (10, -2, 3, -4, 5), create tuple of only positives.
	25.	Create tuple of absolute values for above (use if optional).
	26.	Given t = ("10", "20", "x", "40"), convert numeric strings to int, skip others.
	27.	Given t = (1, None, 2, None, 3), count None using loop.
	28.	Replace None with 0 and make new tuple.
	29.	Given t = (1,2,3,4,5,6,7,8), create tuple of elements at prime indexes.
	30.	Given t = (1,2,3,4,5,6,7,8), create tuple of prime values.
	31.	Given t = (1,2,3,4,5), create tuple of cumulative sums (1,3,6,10,15).
	32.	Given t = (3,3,3,2,2,1), compress into ((3,3),(2,2),(1,1)) (value,count).
	33.	Given t = (1,2,1,2,1,3), remove duplicates keeping first occurrence.
	34.	Remove duplicates keeping last occurrence.
	35.	Given t = (1,2,3,4,5), create pairwise tuple ((1,2),(2,3),(3,4),(4,5)).
	36.	Given t = (1,2,3,4), create ((1,4),(2,3)) (mirror pairing).
	37.	Given t = (1,2,3,4,5), find if it’s palindrome (tuple equals reverse).
	38.	Given t = ("a","b","c"), generate all 2-length pairs (nested loops).
	39.	Given t = (1,2,3), generate all ordered triples (i,j,k) with i!=j!=k.
	40.	Given t = (1,2,3,4), find all pairs whose sum is 5.
	41.	Given tuple of tuples t = (("A",50),("B",70),("C",40)), print grade by marks:
	•	=60: “Pass”, else “Fail”.
	42.	Same as above: add “Distinction” if marks>=75 else “Pass” if >=60 else “Fail”.
	43.	Given t = (("A",50),("B",70),("C",40)), count how many pass.
	44.	Given t = ((101,"X",60000),(102,"Y",45000)), find highest salary employee.
	45.	Given t = ((1,2),(3,4),(5,6)), swap each pair → ((2,1),(4,3),(6,5)).
	46.	Given t = (1, (2,3), 4), flatten one-level (ignore deeper).
	47.	Given t = (("a",1,2),("b",3,4)), sum last two of each and keep key.
	48.	Given t = (1,2,3,4,5,6), split into evens and odds tuples.
	49.	Given t = (5,1,5,2,5,3), find longest streak of 5.
	50.	Given t = (1,2,3,4), create (1,-2,3,-4) using if inside loop.
	51.	Given t = ("hi", "hello", "a", "world"), keep strings length >=3.
	52.	Given t = (1,2,3,4,5), create tuple of differences (2-1, 3-2, ...).
	53.	Given t = (2,3,4,5), compute factorial for each element and store in tuple.
	54.	Given t = (10, 15, 21, 28), count numbers divisible by 3, 5, 7 using elif chain.
	55.	Given t = (1,2,3,4,5), print pattern using tuple values (nested loops).
	56.	Given t = (3,1,2), generate all permutations using loops (no itertools).
	57.	Given t = (1,2,3,4,5), create tuple of running max (1,2,3,4,5) (general case).
	58.	Given t = (5,2,8,1,9), find min and max using loop (no min/max).
	59.	Given t = (1,2,3,4,5), remove middle element (odd length).
	60.	Given t = (1,2,3,4,5,6), remove two middle elements (even length).


# Tuple & LIST 

    61.	Convert list to tuple and tuple to list and show why conversion is needed (example: append).
	62.	Given list of tuples [(1,2),(3,4)], create tuple of sums (3,7).
	63.	Given list of tuples [(101,"A",60),(102,"B",45)], filter pass marks >=50.
	64.	Given tuple of lists ([1,2],[3,4]), modify inner list and explain immutability.
	65.	Given lst=[(1,2),(2,3),(3,4)], create dict using tuple pairs and handle duplicates.
	66.	Given lst=[(1,2),(1,3),(2,4)], group values by key into dict of lists.
	67.	Given lst=[(1,2),(3,4),(5,6)], swap each pair in-place (create new list).
	68.	Given t=(1,2,3), create list of tuples pairing each with its index.
	69.	Given lst=[10,20,30,40], create tuple of (value, “even/odd index”) using if.
	70.	Given list of tuples representing transactions (type, amount), compute balance:
	•	“credit” add, “debit” subtract.
	71.	Same as above: if debit > balance, skip and count rejected debits.
	72.	Given list of tuples (name, age), find oldest and youngest using loop.
	73.	Given lst=[(“A”,90),(“B”,65),(“C”,30)], assign grade A/B/C/F with if-elif.
	74.	Given lst=[(“A”, [10,20]), (“B”, [5,5])], compute total for each name.
	75.	Given list of tuples (city,temp), find average temp per city (duplicates exist).
	76.	Given tuple of numbers, create list of tuples (n, n*n) for only odd n.
	77.	Given list of tuples, sort by second value without using sorted() (manual).
	78.	Given list and tuple, merge and remove duplicates keeping order.
	79.	Given lst=[1,2,3] and t=(4,5), create [(1,4),(2,5)] using zip logic manually.
	80.	Given list of tuples (id, status), count each status (like “SUCCESS”, “FAIL”).
	81.	Given list of tuples (product, price), apply discount rules using if-elif:
	•	price>=1000: 10%, >=500: 5%, else 0%.
	82.	Given lst=[(1,2,3),(4,5,6)], transpose into [(1,4),(2,5),(3,6)].
	83.	Given lst=[(1,2),(3,4),(5,6)], flatten into [1,2,3,4,5,6] using loops.
	84.	Given lst=[(1,"a"),(2,"b"),(3,"c")], build tuple "a","b","c" from it.
	85.	Given lst=[(1,2),(2,1),(3,3)], check if any pair has equal elements

# List & Tuple & Loops 

    86.	Given tuple t, check if it’s strictly increasing, decreasing, or neither (if-elif-else).
	87.	Given tuple t, find first index where increasing order breaks.
	88.	Given tuple t, find all local peaks (element greater than neighbors).
	89.	Given tuple t, create new tuple where each element is sum of neighbors (edge rules).
	90.	Given tuple t, find longest increasing contiguous subsequence length.
	91.	Given tuple t, find longest alternating (up-down-up-down) pattern length.
	92.	Given tuple t, move all zeros to end while keeping relative order (tuple output).
	93.	Given tuple t, treat it as digits and form the largest number ignoring zeros at start.
	94.	Given tuple t of integers, print all triplets whose sum is 0 (nested loops).
	95.	Given tuple t, count pairs (i,j) where t[i] > t[j] and i<j (inversion count, brute force).
	96.	Given tuple t, check if it can be split into two parts with equal sum (loop).
	97.	Given tuple t, find all split points where left sum == right sum.
	98.	Given tuple t of strings, group by first letter into dict of tuples (if key exists append).
	99.	Given tuple t of mixed types, separate into three tuples: ints, floats, strings (use isinstance + if/elif).
	100.	Given tuple t of numbers, simulate “two-sum”: find first pair that equals target, else print “Not found”.



# Senario Based 

    1. Banking Transaction System
	    You receive transactions as a tuple:
        transactions = (("credit", 5000), ("debit", 2000), ("debit", 4000))

        Write logic to:
	•	Maintain balance
	•	Reject debit if insufficient balance
	•	Count rejected transactions


    Add rule:
	•	If debit > 10,000 → flag as “Fraud Alert”
	Print:
	•	Total credits
	•	Total debits
	•	Final balance
	•	Number of rejected transactions


2. Employee Salary Processing

employees = (
    (101, "Anuj", 75000),
    (102, "Rahul", 45000),
    (103, "Priya", 120000),
)


Apply bonus:
	•	Salary > 100000 → 20%
	•	Salary > 50000 → 10%
	•	Else → 5%

	-	Find highest paid employee using loop.
	-	Count how many employees fall in each salary band.


3. Commerce Order Processing

orders = (
    ("Laptop", 80000, 1),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
)

Calculate:
	•	Total bill
	•	Apply discount:
	•	Bill > 100000 → 15%
	•	Bill > 50000 → 10%
	•	Else → 5%

	-	Find most expensive product by price.
	-	Remove products where quantity = 0.


4. Student Result Analytics

    students = (
    ("Aman", 85),
    ("Riya", 72),
    ("Kabir", 55),
    ("Simran", 30),
)

Assign grades:
	•	=90 → A+
	•	=75 → A
	•	=60 → B
	•	=40 → C
	•	Else → Fail

	-	Count how many passed and failed.
	-	Find topper without using max().

5. Delivery Tracking System

deliveries = (
    ("ORD101", "Delivered"),
    ("ORD102", "Pending"),
    ("ORD103", "Cancelled"),
)

Count status occurrences.
	- If more than 3 orders are pending → print “Operational Issue”


6. Stock Market Data

    prices = (100, 105, 102, 108, 110, 107)

    Find:
	•	Maximum profit (buy low sell high)
	•	Count how many days price increased.

	-	Detect if market trend is:

	•	Increasing
	•	Decreasing
	•	Mixed

7. Hospital Patient Records

    patients = (
    ("P1", 102),
    ("P2", 99),
    ("P3", 104),
)

If temperature > 101 → “High Fever”
Else → “Normal”
	-	Count critical patients.


8. Toll Booth System

vehicles = (
    ("Car", 50),
    ("Truck", 150),
    ("Bike", 20),
)

Calculate total toll collected.
	-	If truck count > 5 → print “Heavy Traffic”.


9. Fraud Detection System

tx = (200, 15000, 300, 45000, 100)

If amount > 20000 → flag suspicious.
	-	Count suspicious transactions.


10. Inventory Management

inventory = (
    ("Laptop", 5),
    ("Mouse", 50),
    ("Keyboard", 0),
)

Print items out of stock.
	-	If stock < 10 → “Low Stock Alert”.


11. EMI Payment Tracker

payments = (5000, 5000, 0, 5000, 5000)

If payment = 0 → count missed EMI.
	-	If missed > 2 → mark as defaulter.


12. Data Engineering Monitoring 

file_loads = (
    ("file1.csv", 8395),
    ("file2.csv", 8385),
    ("file3.csv", 8395),
    ("file4.csv", 8397),
)


Detect which file has mismatch from expected count (8395).
	-	Count how many files have mismatched row count.

13. Expense Tracker

expenses = (
    ("Food", 500),
    ("Travel", 2000),
    ("Shopping", 5000),
)


Categorize:
	•	4000 → Luxury
	•	1000 → Moderate
	•	Else → Basic



