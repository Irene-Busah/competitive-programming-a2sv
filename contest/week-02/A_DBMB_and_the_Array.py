"""
DBMB had a birthday yesterday. He was gifted an array a, of n elements and a number x.
But there is one problem: he only likes arrays where the sum of the elements equals s. 
To make the array appealing to him, you can perform the following operation any number of times:

Choose an index t (1≤ t ≤n) and add x to the number ai.
For example, if he was given the array [1,2,3,5] and x=2, you can choose index 3
and get the array [1,2,5,5]. Your task is to determine whether the array can appeal 
to DBMB after any number of operations.

Input
======
Each test consists of several test cases. The first line contains a single integer t(1≤ t ≤1000) — 
the number of test cases. The following describes the test cases.

The first line of each test case contains three integers n, s, x.

The second line of each test case contains n integers a1,a2, (1≤ai≤10) — 
the elements of the array gifted to DBMB.

Output
=======
For each test case, output "YES" if the array can appeal to DBMB. Otherwise, output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings 
"yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
"""


# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the number of test cases
numOfTestCases = getInt()

# getting each test case
for _ in range(numOfTestCases):
    numOfArrayItems, sumOfItems, numToAdd = getIntList()

    dbmb_gift = getIntList()
    total = sum(dbmb_gift)

    while total < sumOfItems:
        total += numToAdd
    
    if total == sumOfItems:
        print("YES")
    else:
        print("NO")
        





