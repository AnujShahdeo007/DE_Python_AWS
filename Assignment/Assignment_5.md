# Assignment 5

employees.txt
101,John,5000
102,Alice,7000
103,Bob,abc
104,Emma,8000
105,David,3000
106,John,5000
107,Chris,6500
108,Sophia,9000
109,Mike,4500
110,Olivia,7000
111,Daniel,
112,Isabella,6200
113,James,3000
114,Mia,abc
115,Noah,7200

116,Liam,5100
117,Ava,8800
118,Ethan,4100
119,John,5000
120,Charlotte,7600
121,Amelia,5400
122,Lucas,bad_data
123,Harper,6100
124,Henry,4700
125,Evelyn,8300



-----------------------------------------------------
employees_day2.txt

101,John,5000
104,Emma,8000
107,Chris,6500
126,Arjun,5500
127,Riya,7800
128,Kabir,4900
129,Meera,9100
120,Charlotte,7600
125,Evelyn,8300
130,Aditya,6200
--------------------------------------------------------

system.log

INFO User login
ERROR Database failed
INFO File uploaded
ERROR Timeout occurred
WARNING Disk space low
ERROR API failed
INFO Job started
WARNING Memory usage high
INFO Job completed
ERROR Invalid credentials
INFO User logout
DEBUG Cache refreshed
CRITICAL Server down
WARNING CPU threshold exceeded
ERROR Network failure


------------------------------------------------------------

students.txt

201,Rahul,78
202,Anjali,91
203,Vikram,45
204,Priya,88
205,Amit,abc
206,Neha,67
207,Karan,32
208,Simran,99
209,Rohit,54
210,Sneha,40
211,Arun,
212,Meena,73
213,Varun,29
214,Pooja,85
215,Kirti,bad

---------------------------------------------------------------

products.txt

P101,Laptop,55000,Electronics
P102,Mouse,700,Electronics
P103,Chair,3500,Furniture
P104,Table,6200,Furniture
P105,Phone,abc,Electronics
P106,Bottle,500,Kitchen
P107,Sofa,25000,Furniture
P108,Headphones,1800,Electronics
P109,Plate,300,Kitchen
P110,Microwave,12000,Kitchen
P111,TV,45000,Electronics
P112,Bed,,Furniture
P113,Fan,2800,Electronics
P114,Oven,bad,Kitchen
P115,Lamp,1500,Furniture



Q1. Count total employee records

Use employees.txt.

Task:

count total non-empty lines


Q2. Print only employee names

Use employees.txt.

Task:

read file
print only names column


Q3. Print only valid salary rows

Use employees.txt.

Task:

print only rows where salary is numeric


Q4. Count invalid salary rows

Use employees.txt.

Task:

count rows like abc, blank salary, bad_data
Q5. Print employees with salary greater than 5000

Use employees.txt.

Task:

apply condition
print matching rows
Q6. Print employees whose ID is even

Use employees.txt.

Task:

convert ID to int
check even/odd


Q7. Skip empty lines

Use employees.txt.

Task:

ignore blank rows while reading


Q8. Print line numbers with invalid data

Use employees.txt.

Task:

for every bad row, print line number and content


Q9. Count total log lines

Use system.log.

Task:

count all non-empty log lines


Q10. Print only WARNING lines

Use system.log.

Task:

filter log lines using condition



Section 2: List Concepts

Q11. Store all employee lines in a list

Use employees.txt.

Task:

read file
store each non-empty line in a list
Q12. Store only valid employee names in a list

Use employees.txt.

Task:

build list of names where salary is valid

Expected idea:

["John", "Alice", "Emma", ...]


Q13. Store valid salaries in a list and find max salary

Use employees.txt.

Task:

create salary list
find highest salary
Q14. Store employee tuples in a list

Use employees.txt.

Task:

for valid rows create:
(emp_id, name, salary)
store in a list


Q15. Build a list of employees whose salary is above average

Use employees.txt.

Task:

calculate average from valid salaries
create filtered list
Section 3: Dictionary Concepts
Q16. Convert valid employee data into list of dictionaries

Use employees.txt.

Task:

each valid row becomes:
{"id": 101, "name": "John", "salary": 5000}


Q17. Create name to salary mapping

Use employees.txt.

Task:

build dictionary:
{"John": 5000, "Alice": 7000}

Note:
duplicate names exist, so observe overwrite behavior

Q18. Count employees by salary range

Use employees.txt.

Task:
Create dictionary like:

{
  "low": count_of_salary_below_5000,
  "medium": count_of_salary_5000_to_7000,
  "high": count_of_salary_above_7000
}


Q19. Count log levels in dictionary

Use system.log.

Task:
Create:

{"INFO": 5, "ERROR": 4, "WARNING": 3, "DEBUG": 1, "CRITICAL": 1}


Q20. Group products by category

Use products.txt.

Task:
Create dictionary like:

{
  "Electronics": [...],
  "Furniture": [...],
  "Kitchen": [...]
}



Section 4: Tuple Concepts


Q21. Create tuple records for students

Use students.txt.

Task:

valid rows only
make tuple:
(student_id, name, marks)



Q22. Find highest scoring student using tuples

Use students.txt.

Task:

build tuple list
find max marks



Q23. Create tuple of unique product categories

Use products.txt.

Task:

extract categories
convert to tuple

Expected idea:

("Electronics", "Furniture", "Kitchen")



Q24. Store (name, result) tuple for students

Use students.txt.

Task:

result = Pass if marks >= 40 else Fail
store as tuple list



Q25. Create tuple of employees with salary > 7000

Use employees.txt.

Task:

filtered tuple records only
Section 5: Set Concepts
Q26. Find unique employee names

Use employees.txt.

Task:

create set of names




Q27. Find duplicate employee names

Use employees.txt.

Task:

use set logic to identify repeated names

Hint:
John appears multiple times



Q28. Find common employee IDs between employees.txt and employees_day2.txt

Use both files.

Task:

build 2 sets of IDs
find intersection



Q29. Find employee IDs present in employees.txt but not in employees_day2.txt

Use both files.

Task:

set difference



Q30. Find unique log levels in system.log

Use system.log.

Task:

extract first word from each line
store in set

Expected idea:

{"INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"}



Bonus Real-Time Project Questions

These are bigger scenario-based tasks using the same files.

Bonus Q31. Employee salary processor

Use employees.txt.

Task:

valid rows only
calculate bonus:
salary > 7000 → 20%
salary >= 5000 → 10%
else → 5%
create output file:
ID,Name,Salary,Bonus,Total
write errors in app.log
Bonus Q32. Student result generator

Use students.txt.

Task:

assign result and grade
create result.txt
invalid rows should go to invalid_students.txt

Grade:

90+ A
75–89 B
40–74 C
below 40 Fail
Bonus Q33. Log analyzer

Use system.log.

Task:

count all log levels
write summary to summary.txt
write only errors to error.log
Bonus Q34. Product category report

Use products.txt.

Task:

skip invalid price rows
group by category
count items in each category
find highest price product in each category
Bonus Q35. Employee comparison report

Use employees.txt and employees_day2.txt.

Task:

common employee IDs
new employee IDs in day2
missing employee IDs from day1
write final comparison report


------------------------------------------------------------------------------------------------------------------------------

Q36. Data Cleaning Pipeline

Use employees.txt

Task:

Read file
Separate into:
valid_employees.txt
invalid_employees.txt
Invalid if:
salary not numeric
missing fields
Q37. Deduplicate Employees

Use employees.txt

Task:

Remove duplicate employee records
Write unique records to unique_employees.txt
Q38. Salary Normalization

Use employees.txt

Task:

Increase all valid salaries by 5%
Save to normalized_salary.txt
Q39. Salary Band Tagging

Use employees.txt

Task:
Add band:

<5000 → LOW
5000–7000 → MEDIUM

7000 → HIGH

Output:

101,John,5000,MEDIUM
Q40. Employee Summary Report

Use employees.txt

Output:

Total employees: X
Valid employees: X
Invalid employees: X
Avg salary: X
Max salary: X
Min salary: X


Section 2: Cross File Scenarios
Q41. Incremental Data Detection

Use employees.txt and employees_day2.txt

Task:

Find new employees in Day2
Find removed employees
Write both lists
Q42. Merge Employee Files

Use both files

Task:

Combine both files
Remove duplicates
Output merged file
Q43. Salary Comparison Report

Use both files

Task:

Compare salary changes (if same ID exists)
Output:
ID,Old Salary,New Salary,Difference
Section 3: Log-Based Scenarios (VERY IMPORTANT)


Q44. Error Rate Calculation

Use system.log

Task:

Calculate % of ERROR logs
Q45. Extract Critical Logs

Use system.log

Task:

Write all ERROR + CRITICAL logs into critical.log

Q46. Log Timeline Simulation

Use system.log

Task:

Assign line numbers as timestamps
Store logs in dictionary:
{1: "INFO User login", 2: "ERROR Database failed"}
Q47. Alert Generator

Use system.log

Task:

If ERROR count > 3 → print ALERT
Else → print NORMAL
Q48. Log Level Ranking

Use system.log

Task:

Count logs
Sort by highest frequency
Section 4: Student Processing Scenarios
Q49. Topper Finder

Use students.txt

Task:

Find student with highest marks
Q50. Fail Student Extractor

Use students.txt

Task:

Extract students with marks < 40
Save to fail_students.txt


Q51. Grade Distribution

Use students.txt

Output:

{"A": 2, "B": 3, "C": 4, "Fail": 2}

Q52. Average Marks Calculator

Use students.txt

Task:

Calculate average marks (ignore invalid rows)
Q53. Student Ranking System

Use students.txt

Task:

Sort students by marks
Print top 5

Section 5: Product Scenarios


Q54. Category Revenue Calculation

Use products.txt

Task:

Sum prices per category


Q55. Expensive Products Filter

Use products.txt

Task:

Print products with price > 10000


Q56. Invalid Product Extractor

Use products.txt

Task:

Extract rows with invalid price

Q57. Cheapest Product per Category

Use products.txt

Task:

Find lowest price product in each category

Q58. Product Inventory Report

Use products.txt

Output:

Total products: X
Valid products: X
Invalid products: X

Section 6: Mixed Concepts (VERY IMPORTANT)

Q59. Build Master Data Structure

Use employees.txt

Task:

Store all valid employees in:
{
  "101": {"name": "John", "salary": 5000}
}
Q60. Unique Salary Finder

Use employees.txt

Task:

Use set to find unique salaries

Q61. Salary Frequency Counter

Use employees.txt

Output:

{5000: 3, 7000: 2}

Q62. Multi-Condition Filter

Use employees.txt

Task:

salary > 5000 AND name starts with 'J'


Q63. Batch Processing Simulation

Use employees.txt

Task:

Process file in chunks of 5 lines

Section 7: Real Pipeline Simulation

Q64. Mini ETL Pipeline (VERY IMPORTANT)

Use employees.txt

Steps:
Read file
Clean data
Transform (add bonus)
Store in list of dict
Write to output file
Log errors

Q65. Audit Logging System

Every step:

read
validate
transform

Write logs into app.log

Q66. File Comparator Tool

Compare 2 files:

common records
missing records
extra records
