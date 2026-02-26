"""

You are given the array a consisting of n positive (greater than zero) integers.

In one move, you can choose two indices i and j (𝑖≠𝑗) such that the absolute difference between ai
and aj is no more than one (|ai-aj|≤1) and remove the smallest of these two elements. 
If two elements are equal, you can remove any of them (but exactly one).

Your task is to find if it is possible to obtain the array consisting of only one element 
using several (possibly, zero) such moves or not.

You have to answer t independent test cases.

Input
=====
The first line of the input contains one integer t (1≤t≤1000) — the number of test cases. Then t
test cases follow.

The first line of the test case contains one integer n (1≤n≤50) — the length of a.
The second line of the test case contains n integers a1,a2,…,an (1≤ai≤100), where ai
is the i-th element of a.


Output
======
For each test case, print the answer: "YES" if it is possible to obtain the array consisting 
of only one element using several (possibly, zero) moves described in the problem statement, 
or "NO" otherwise.


size = len(array)
for i in range(size):
min_idx = i
for j in range(i + 1, size):
if array[min_idx] >= array[j]:
min_idx = j
array[i], array[min_idx] = array[min_idx], array[i]
return array

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
    lenOfArray = getInt()

    array = getIntList()

    array.sort()

    okay = True

    for i in range(1, lenOfArray):
        if array[i] - array[i-1] > 1:
            okay = False
            break

    print("YES" if okay else "NO")
