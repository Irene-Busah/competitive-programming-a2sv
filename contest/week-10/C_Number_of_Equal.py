"""
You are given two arrays a and b, sorted in non-decreasing order. Find the number of 
pairs (i,j) for which ai=bj.

Input
The first line contains integers n and 𝑚, the sizes of the arrays (1≤n,𝑚≤10^5). 
The second line contains n integers ai, elements of the first array, the third 
line contains 𝑚 integers bi, elements of the second array (-10^9≤ai,bi≤10^9).

Output
Print one number, the answer to the problem.
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

first, second = 0, 0

count = 0


while first < n and second < m:
    if array1[first] < array2[second]:
    
        first += 1
        
    elif array1[first] > array2[second]:
        second += 1
    else:
        val = array1[first]
        count1 = 0
        while first < n and array1[first] == val:
            count1 += 1
            first += 1
        
        count2 = 0
        while second < m and array2[second] == val:
            count2 += 1
            second += 1
        
        count += count1 * count2

print(count)

