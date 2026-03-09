"""
For educational purposes, in the problems of this block, the time limit is large enough for the solution 
to pass in O(nlogn) time, but try to write the solution in linear time, which we discussed in the lecture.

You are given two arrays, sorted in non-decreasing order. Merge them into one sorted array.

Input
=====
The first line contains integers n and 𝑚, the sizes of the arrays (1≤n,𝑚≤10^5). The second 
line contains n integers ai, elements of the first array, the third line contains 𝑚 integers bi, 
elements of the second array (-109≤ai,bi≤109).

Output
======
Print n+𝑚 integers, the merged array.
"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


n, m = getIntList()

array1 = getIntList()
array2 = getIntList()

res = []

first = 0
second = 0

while first < n and second < m:
    if array1[first] <= array2[second]:
        res.append(array1[first])
        first += 1
    else:
        res.append(array2[second])
        second += 1

res.extend(array1[first:])
res.extend(array2[second:])
print(*res)
    


