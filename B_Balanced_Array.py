"""
You are given a positive integer n, it is guaranteed that n is even (i.e. divisible by 2).

You want to construct the array a of length n such that:

The first n/2 elements of a are even (divisible by 2);
the second n/2 elements of a are odd (not divisible by 2);
all elements of a are distinct and positive;
the sum of the first half equals to the sum of the second half 
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
    num = getInt()

    array = []

    


