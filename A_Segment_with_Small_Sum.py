"""
Given an array of n integers ai. Let's say that the segment of this array a[l..r]
(1≤l≤r≤n) is good if the sum of elements on this segment is at most S. 
Your task is to find the longest good segment.

Input
The first line contains integers n and s (1≤n≤105, 1≤s≤1018). The second line 
contains integers ai (1≤ai≤10^9).

Output
Print one integer, the length of the longest good segment. If there are no such segments, print 0
"""


# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


n, s = getIntList()

array = getIntList()

left = 0
sumOfSegment = 0

longest = 0

for right in range(n):
    sumOfSegment += array[right]

    while sumOfSegment > s:
        sumOfSegment -= array[left]

        left += 1
    

    longest = max(longest, right - left + 1)

print(longest)


