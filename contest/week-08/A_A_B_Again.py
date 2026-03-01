"""
Given a two-digit positive integer n, find the sum of its digits.

Input
=====
The first line contains an integer t(1≤t≤90) — the number of test cases.

The only line of each test case contains a single two-digit positive integer n
(10≤n≤99).

Output
======
For each test case, output a single integer — the sum of the digits of n
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the data input
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    number = getInt()

    remainder = number % 10

    val = number // 10

    res = remainder + val

    print(res)


