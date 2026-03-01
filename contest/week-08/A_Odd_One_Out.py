"""
You are given three digits a, b, c. Two of them are equal, but the third one is different
from the other two.

Find the value that occurs exactly once.

Input
=====
The first line contains a single integer t (1≤t≤270
) — the number of test cases.

The only line of each test case contains three digits a, b, c (0≤a, b, c≤9). 
Two of the digits are equal, but the third one is different from the other two.

Output
=======
For each test case, output the value that occurs exactly once.
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

    counter = {}

    for i in range(len(array)):
        if array[i] not in counter:
            counter[array[i]] = 1
        else:
            counter[array[i]] += 1

    for key, val in counter.items():
        if val == 1:
            print(key)

    # print(counter)


