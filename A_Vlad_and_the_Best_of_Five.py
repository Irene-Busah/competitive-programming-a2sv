"""
Vladislav has a string of length 5, whose characters are each either A or B.

Which letter appears most frequently: A or B?

Input
The first line of the input contains an integer t (1≤t≤32) — the number of test cases.

The only line of each test case contains a string of length 5 consisting of letters A and B.

All t strings in a test are different (distinct).

Output
======
For each test case, output one letter (A or B) denoting the character that appears most 
frequently in the string.
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



# getting input data
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    string = getStr()

    counter = {}

    for i in range(len(string)):
        if string[i] not in counter:
            counter[string[i]] = 1
        else:
            counter[string[i]] += 1
    

    maxVal = 0
    ans = ''
    for key, val in counter.items():
        if val > maxVal:
            maxVal = val
            ans = key

    print(ans)