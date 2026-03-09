"""
You are given two arrays, sorted in non-decreasing order. For each element of the second array, 
find the number of elements in the first array strictly less than it.

Input
=====
The first line contains integers n and 𝑚, the sizes of the arrays (1≤n,𝑚≤10^5). 
The second line contains n integers am, elements of the first array, the third line contains 𝑚 
integers bi, elements of the second array (-10^9≤ai,bi≤10^9).

Output
Print 𝑚 numbers, the number of elements of the first array less than each of the elements 
of the second array.
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

first = 0

res = []

for second in range(m):
    while first < n and array1[first] < array2[second]:
        first += 1

    res.append(first)

print(*res)


