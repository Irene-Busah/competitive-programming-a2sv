"""
Codeforces separates its users into 4
 divisions by their rating:

For Division 1: 1900≤rating
For Division 2: 1600≤rating≤1899
For Division 3: 1400≤rating≤1599
For Division 4: rating≤1399
Given a rating, print in which division the rating belongs.

Input
The first line of the input contains an integer t (1≤t≤10^4) — the number of testcases.

The description of each test case consists of one line containing one integer rating 
(-5000≤rating≤5000).

Output
For each test case, output a single line containing the correct division in the format 
"Division X", where X is an integer between 1 and 4 representing the division for the 
corresponding rating.
"""


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


for _ in range(numOfTestCases):
    rating = getInt()

    if rating <= 1399:
        print("Division 4")
    elif rating >= 1400 and rating <= 1599:
        print("Division 3")
    elif rating >= 1600 and rating <= 1899:
        print("Division 2")
    else:
        print("Division 1")

