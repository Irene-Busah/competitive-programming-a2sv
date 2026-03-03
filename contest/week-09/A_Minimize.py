"""
You are given two integers a and b(𝑎≤𝑏). Over all possible integer values of c (𝑎≤𝑐≤𝑏), 
find the minimum value of (c-a)+(b-c).

Input
The first line contains t (1≤t≤55) — the number of test cases.

Each test case contains two integers a and b (1≤a≤b≤10).

Output
For each test case, output the minimum possible value of (c-a)+(b-a) on a new line.
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

for i in range(numOfTestCases):
    a, b = getIntList()

    c = b - a

    print(c)



