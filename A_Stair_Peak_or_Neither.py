"""
You are given three digits a, b, and c. Determine whether they form a stair, a peak, or neither.

    - A stair satisfies the condition a<b<c
    - A peak satisfies the condition a<b>c

Input
=====
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The only line of each test case contains three digits a, b, c (0≤a, b, c≤9).

Output
For each test case, output "STAIR" if the digits form a stair, "PEAK" if the digits 
form a peak, and "NONE" otherwise (output the strings without quotes).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    a, b, c = getIntList()

    if a < b and b < c:
        print("STAIR")
    elif a < b and b > c:
        print("PEAK")
    else:
        print("NONE")


