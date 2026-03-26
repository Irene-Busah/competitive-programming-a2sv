"""
Given an integer n, find an integer x such that: 2≤x≤n.
The sum of multiples of x that are less than or equal to n is maximized. Formally, x+2x+3x+⋯+kx 
where 𝑘𝑥≤𝑛 is maximized over all possible values of x

Input
The first line contains t (1≤t≤100) — the number of test cases.

Each test case contains a single integer n (2≤n≤100).

Output
For each test case, output an integer, the optimal value of x. It can be shown there is only one unique answer.
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
    n = getInt()

    best_x = 2
    max_sum = 0

    for x in range(2, n+1):
        k = n // x
        s = x * k * (k + 1) // 2

        if s > max_sum:
            max_sum = s
            best_x = x

    print(best_x)

