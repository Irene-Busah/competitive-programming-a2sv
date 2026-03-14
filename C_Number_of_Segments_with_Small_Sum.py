"""
Given an array of n integers ai. Let's say that the segment of this array a[l..r]
(1≤l≤r≤n) is good if the sum of elements on this segment  is at most s.

Your task is to find the number of good segments.

Input
The first line contains integers n and s (1≤n≤105, 1≤s≤1018). The second line contains integers ai (1≤ai≤109).

Output
Print one integer, the number of good segments.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# n, s = getIntList()

# array = getIntList()

# left = 0
# segmentSum = 0
# count = 0

# for right in range(n):
#     segmentSum += [right]

#     while segmentSum <= s and left <= right:
#         count += 1


