"""
Given three distinct integers a, b, and c, find the medium number between all of them.

The medium number is the number that is neither the minimum nor the maximum of the given 
three numbers.

For example, the median of 5,2,6 is 5, since the minimum is 2 and the maximum is 6


Input
=====
The first line contains a single integer t (1≤t≤6840) — the number of test cases.

The description of each test case consists of three distinct integers a, b, c(1≤a,b,c≤20).

Output
======
For each test case, output a single integer — the medium number of the three numbers.
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
    array = getIntList()

    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    mid = len(array) // 2
    # print(array)
    print(array[mid])

