"""
You are given three integers a, b, and c such that exactly one of these two equations is true:

    - a+b=c
    - a-b=c
Output + if the first equation is true, and - otherwise.


Input
=====
The first line contains a single integer t (1≤t≤162) — the number of test cases.

The description of each test case consists of three integers a, b, c (1≤a,b≤9, -8≤c≤18). 
The additional constraint on the input: it will be generated so that exactly one of the two equations will be true.

Output
======
For each test case, output either + or - on a new line, representing the correct equation.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the input data
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    a, b, c = getIntList()

    if sum([a, b]) == c:
        print("+")
    else:
        print("-")



