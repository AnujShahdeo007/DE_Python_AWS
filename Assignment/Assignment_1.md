# Assignment 1

1.	Clean API ages
Input: ages = ["25", "30", "", None, "18", " 40 "]
Task: remove invalid values ("", None, non-digits), strip spaces, convert to int, print len/min/max/sum.

2.	Normalize names
Input: names = [" anuj", "AMIT ", "", "riya", None]
Task: remove invalid, strip, title-case using loops, create final list.

3.	Validate all emails contain “@”
Input: list of emails
Task: using loop + condition build list of invalid emails; print any(invalid) and all(valid).

4.	Remove negative prices
Input: prices = [100, -5, 200, 0, 50]
Task: keep only >0, then insert missing default price 99 at index 0 if list becomes empty.

5.	Keep only numeric strings
Input: vals = ["10", "x", "20", "30a", "40"]
Task: output only numbers as int.

6.	Trim long comments
Input: list of strings
Task: if length > 20, keep first 20 chars + “…”, else keep as is.

7.	Drop duplicates while preserving order
Input: list with duplicates
Task: create unique list using loops (no set).

8.	Split valid/invalid based on rule
Input: records = ["ID-100", "ID-2", "ABC", "ID-999"]
Rule: valid if starts with "ID-" and last part is digits. Separate two lists.

9.	Ensure at least one “ERROR” exists
Input: logs list
Task: print message if any(log == "ERROR") else append "ERROR".

10.	Ensure all values are within range
Input: scores
Task: check all are 0<=score<=100. If not, build list of bad indexes using enumerate.

11.	Find first occurrence index (manual)
Input: list and target
Task: return first index using loop; if not found return -1 (don’t use .index()).
12.	Find all indices of an element
Input: arr = [7,1,7,2,7] target=7
Task: output [0,2,4] using enumerate.
13.	Find second highest number
Input: list of ints
Task: find second max using loop (no sort), handle duplicates.
14.	Find longest word and its index
Input: list of words
Task: return word + index.
15.	Find first string containing substring
Input: list of messages, substring "fail"
Task: print first matching message and index.
16.	Search by prefix
Input: list of S3 keys, prefix "raw/"
Task: create list of only those keys + count.
17.	Search without case sensitivity
Input: names list, search "anuj"
Task: find matching index ignoring case.
18.	Find missing number from 1..n
Input: list containing 1..n except one missing
Task: find missing using sum formula + loop check.
19.	Find most frequent element
Input: list
Task: compute frequencies using loops and return max frequency element.
20.	Find all strings of length exactly 5
Input: list of strings
Task: output list + count.


21.	Add GST to order amounts
Input: list of order totals
Task: create new list with 18% added (loop). (Optional: map)
22.	Convert timestamps strings to standard format
Input: ["2026/01/01", "2026/02/15"]
Task: convert to "YYYY-MM-DD" using split logic.
23.	Mask phone numbers
Input: ["9876543210", "9123456780"]
Task: output ["******3210", "******6780"].
24.	Uppercase only error logs
Input: logs with mixed case
Task: if log contains "error" anywhere, convert to "ERROR" else keep original.
25.	Replace empty city with “UNKNOWN”
Input: cities list with ""
Task: replace empties.
26.	Map numbers to pass/fail
Input: marks
Rule: pass if >=40
Output: ["PASS","FAIL",...]
27.	Create running total list
Input: [10,20,5]
Output: [10,30,35]
28.	Extract domain from emails
Input: ["a@x.com","b@y.in"]
Output: ["x.com","y.in"]
29.	Split full names into first names
Input: ["Hello kumar", "Amit Kumar"]
Output: ["Hello","Amit"]
30.	Convert mixed numeric list to integers safely
Input: [1, "2", "03", "x"]
Task: keep only numeric convert to int.

31.	Sort orders descending without modifying original
Use sorted() and show original unchanged.
32.	Sort words by length
Input words list
Output sorted by length using loop-based key or sorted(key=len).
33.	Top 3 highest values (no sort allowed)
Find top 3 using loops.
34.	Rank students by marks
Input: students list + marks list
Task: combine via zip, sort by marks descending, add rank using enumerate(start=1).
35.	Stable sort simulation
Input: list of (name, score) with ties
Task: keep original order for ties (explain stable sort, use sorted).
36.	Reverse list without changing original
Use reversed() and list() conversion.
37.	Rotate list right by k
Input list, k
Output rotated list using slicing or loop.
38.	Sort only even numbers, keep odds in place
Example: [5,2,8,1,4]
Evens sorted -> [4,8,2]? (Students must keep odd positions unchanged.)


39.	Merge two columns into records
names + cities → list of tuples using zip.
40.	Create dictionary using zip
keys list + values list → dict (students can build via loop).
41.	Compare two lists element-wise
a and b same size: output list of "MATCH"/"DIFF" using loop + zip.
42.	Calculate total price from qty & price lists
qty list and price list
Output line totals using zip and multiplication, then sum totals.

43.	Find mismatched pairs
Given usernames list and status list, find all where status != “ACTIVE”.

44.	Pad shorter list manually (no zip_longest)
Two lists different sizes
Task: extend shorter with default "NA" using loop, then zip.

45.	Transpose 2D list (matrix)
Input: [[1,2,3],[4,5,6]]
Output transposed using zip(*matrix) OR manual loops.


46.	Use insert to place header
Input: list of rows
Task: insert "HEADER" at index 0.

47.	Use remove safely
If "TEMP" exists in list remove it once else do nothing (avoid ValueError using condition).

48.	Use pop to process stack
Input: tasks list
While tasks not empty, pop last and print processed.

49.	Use extend to merge batches
batch1 + batch2 + batch3 merge into one list.

50.	Use clear to reset after processing
After computing summary metrics, clear list and show it’s empty.
51.	Use copy to create backup before modifications
Create backup copy then sort original; show backup unchanged.
52.	Manual implementation of count()
Count how many times "ERROR" appears using loop.
53.	Manual implementation of index()
Return index of first "WARN" using loop, else -1.
54.	Remove all occurrences of value
Remove all "NA" from list (loop approach).
55.	Deduplicate + preserve first occurrences only
Create list of unique items and also list of duplicates found.


56.	Sessionization (simplified)
Input: list of event times (minutes) sorted
Rule: new session if gap > 30
Output: list of sessions as list of lists.
57.	Split logs by severity
Input: logs like "2026-01-01|ERROR|msg"
Task: create 3 lists: errors, warns, infos (parse using split).
58.	Chunking for batch API calls
Input list of 103 ids
Task: split into batches of size 25 (list of lists).
59.	Detect anomalies
Input numeric list
Rule: anomaly if value > (avg * 2)
Compute avg using sum/len, return anomalies with indices using enumerate.
60.	Build a simple leaderboard
Input: player list, score list
Combine, sort desc, output top N, also show lowest player.

61.	Remove elements at even indices (use enumerate).
62.	Keep only palindromes from list of strings.
63.	Convert list of dicts to list of "id:name" strings.
64.	Find common elements between two lists (no set).
65.	Find elements in A not in B (no set).
66.	Validate passwords list (min length 8, contains digit).
67.	Merge two sorted lists into one sorted list (classic).
68.	Compress runs: ["a","a","b","b","b"] → ["a2","b3"].
69.	Expand runs: ["a2","b3"] → ["a","a","b","b","b"].
70.	Compute pairwise differences: [10,15,13] → [5,-2].




Senario based questions:
--------------------------

Question 1 — Data Cleaning Pipeline 

You receive user ages from API:

ages = ["25", "30", "", "18", None, "40"]

Task
	1.	Remove empty and None values using filter().
	2.	Convert remaining to integers using map().
	3.	Add new age 50 using append().
	4.	Sort ages.
	5.	Print:
	    •	total users (len)
	    •	max age
	    •	min age
	    •	sum of ages

Question 2 — E-commerce Order Processing 

orders = [1000, 2500, 500, 1200, 800]

Task
	1.	Add 18% tax using map().
	2.	Remove orders below 1000 using filter().
	3.	Insert priority order 5000 at index 0.
	4.	Find index of highest order.
	5.	Reverse list using reversed() (without modifying original).


Question 3 — Log Analysis
logs = ["INFO", "ERROR", "INFO", "WARN", "ERROR", "DEBUG"]

Task
	1.	Count number of "ERROR" using count().
	2.	Convert all logs to uppercase using map().
	3.	Check:
	    •	if any ERROR exists (any)
	    •	if all logs are INFO (all)
	4.	Remove first DEBUG using remove().


Question 4 — Student Ranking System 

students = ["Anuj", "Amit", "Riya"]
marks    = [90, 80, 95]

Task
	1.	Combine using zip().
	2.	Sort by marks using sorted().
	3.	Add rank numbers using enumerate(start=1).
	4.	Convert result into list.


Question 5 — ETL File Path Generator 


files = ["data1.csv", "data2.csv", "data3.csv"]

Task
	1.	Generate S3 paths using map().
	2.	Copy original list using copy().
	3.	Extend list with backup files.
	4.	Reverse final list.


Question 6 — Inventory Management

items = ["pen", "book", "laptop", "pen", "mouse", "book"]

Task
	1.	Remove duplicates using list + append() logic.
	2.	Count frequency using count().
	3.	Sort alphabetically.
	4.	Find index of "laptop".
	5.	Pop last item and print it.


Question 7 — Sensor Data Transformation 

sensor = [12.5, 14.2, 10.1, 16.0, 11.7]

Task
	1.	Increase all values by +0.5 using map().
	2.	Filter values greater than 12.
	3.	Sort descending.
	4.	Check if all values are valid (>10).

Question 8 — API Response Flattening 

data = [
    {"id":1,"name":"A"},
    {"id":2,"name":"B"},
    {"id":3,"name":"C"}
]

Task
	1.	Extract all ids using map().
	2.	Extract all names.
	3.	Combine ids and names using zip().
	4.	Convert to list.

Question 9 — Real-Time Dashboard Validation 

values = [100, 200, -10, 300, 0]

Task
	1.	Filter invalid values (<=0).
	2.	Check using:
	    •	any() if negative exists
	    •	all() if valid
	3.	Add fallback value using insert().

Question 10 — Complex List Transformation 

raw = ["  anuj ", " AMIT", "riya  ", ""]

Task
	1.	Remove empty values using filter().
	2.	Strip spaces using map(str.strip).
	3.	Capitalize names.
	4.	Enumerate names starting from 1.
	5.	Convert result into list of tuples.


Question 11:

ids   = [101,102,103,104]
names = ["Amit","Riya","Gaurav"]
city  = ["kolkata","Delhi","Pune","Goa","Mumbai"]

Task
	1.	Combine all using zip().
	2.	Convert to list.
	3.	Use zip_longest() (extra credit).
	4.	Print reversed records.
	5.	Validate using any() / all().




