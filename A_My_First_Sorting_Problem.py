"""
You are given two integers x and y


Output two integers: the minimum of x and y, followed by the maximum of x and y.

Input
The first line contains a single integer t (1≤t≤100) — the number of test cases.

The only line of each test case contains two space-separated integers x and y (0≤x,y≤9).

Output
For each test case, output two integers: the minimum of x and y, followed by the maximum of x and y.
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
    x, y = getIntList()

    if x > y:
        print(y, x)
    else:
        print(x, y)



