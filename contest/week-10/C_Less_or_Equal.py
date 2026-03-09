"""
You are given a sequence of integers of length n and integer number k. You should print any integer number x
in the range of [1;109] (i.e. 1≤x≤10^9) such that exactly k elements of given sequence are less than or equal to x


Note that the sequence can contain equal elements.

If there is no such x, print "-1" (without quotes).

Input
=====
The first line of the input contains integer numbers n and k (1≤n≤2⋅10^5, 0≤k≤n). The second line of the input contains n
integer numbers a1,a2,…,an (1≤ai≤10^9) — the sequence itself.

Output
Print any integer number x from range [1;10^9] such that exactly k elements of given sequence is less or equal to x


If there is no such x, print "-1" (without quotes).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the data
n, k = getIntList()

array = getIntList()
array.sort()

if k == 0:
    if array[0] == 1:
        print(-1)
    else:
        print(array[0] - 1)
    
else:
    x = array[k - 1]
    if k == n or x < array[k]:
        print(x)
    elif x < array[k]:
        print(array[k] - 1)
    else:
        print(-1)





