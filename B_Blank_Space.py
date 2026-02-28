"""
You are given a binary array a of n elements, a binary array is an array consisting only of 0s and 1s.

A blank space is a segment of consecutive elements consisting of only 0s.

Your task is to find the length of the longest blank space.

Input
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤100) — the length of the array.

The second line of each test case contains n space-separated integers ai (0≤n≤1) — the elements of the array.

Output
For each test case, output a single integer — the length of the longest blank space.
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
    lenOfArray = getInt()

    array = getIntList()

    numOfConsecutiveZeros = 0
    best = 0

    for i in range(lenOfArray):
        if array[i] == 0:
            numOfConsecutiveZeros += 1
            best = max(best, numOfConsecutiveZeros)
        else:
            numOfConsecutiveZeros = 0
    
    print(best)



