"""
You are given an array a onsisting of n (n≥3) positive integers. It is known that in this 
array, all the numbers except one are the same (for example, in the array [4,11,4,4]
all numbers except one are equal to 4).

Print the index of the element that does not equal others. The numbers in the array are 
numbered from one.

Input
The first line contains a single integer t (1≤t≤100). Then t test cases follow.

The first line of each test case contains a single integer n (3≤n≤100) — 
the length of the array a


The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100).

It is guaranteed that all the numbers except one in the a array are the same.

Output
For each test case, output a single integer — the index of the element that is 
not equal to others.
"""



import sys
from typing import Counter


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
    lenOfArray = getInt()

    array = getIntList()

    counter = Counter(array)

    val = 0

    for key, value in counter.items():
        if value == 1:
            val = key
    
    print(array.index(val) + 1)



    # for indx, val in enumerate(array):
    #     counter[indx] = val
    #     print(indx, val)




