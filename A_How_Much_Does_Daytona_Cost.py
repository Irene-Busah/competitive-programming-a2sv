"""
We define an integer to be the most common on a subsegment, if its number of occurrences on that subsegment is 
larger than the number of occurrences of any other integer in that subsegment. A subsegment of an array is a 
consecutive segment of elements in the array a.

Given an array a of size n, and an integer k, determine if there exists a non-empty subsegment of a
where k is the most common element.

Input
=====
Each test consists of multiple test cases. The first line contains a single integer t (1≤t≤1000) — 
the number of test cases. The description of test cases follows.

The first line of each test case contains two integers n and k (1≤n≤100, 1≤k≤100) — 
the number of elements in array and the element which must be the most common.

The second line of each test case contains n integers a1, a2, a3, …, an (1≤ai≤100) — elements of the array.

Output
======
For each test case output "YES" if there exists a subsegment in which k is the most common element, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized 
as a positive answer).
"""


from itertools import count
import sys
from typing import Counter


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number test cases
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    numOfElements, element = getIntList()

    array = getIntList()

    b = [1 if x == element else -1 for x in array]

    ok = False
    for i in range(numOfElements):
        s = 0
        for j in range(i, numOfElements):
            s += b[j]
            if s > 0:
                ok = True
                break
        if ok:
            break

    print("YES" if ok else "NO")




