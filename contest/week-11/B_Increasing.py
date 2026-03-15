"""
You are given an array a of n positive integers. Determine if, by rearranging the elements, you can make the 
array strictly increasing. In other words, determine if it is possible to rearrange the elements such that a1<a2<⋯<an
holds.

Input
=====
The first line contains a single integer t (1≤t≤100) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤100) — the length of the array.

The second line of each test case contains n integers ai (1ai≤109) — the elements of the array.

Output
For each test case, output "YES" (without quotes) if the array satisfies the condition, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""


from enum import Flag
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
    numOfElements = getInt()

    array = getIntList()

    array.sort()

    possible = True

    for i in range(1, numOfElements):
        if array[i] <= array[i-1]:
            possible = False
            break
    
    print("YES" if possible else "NO")







