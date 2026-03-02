"""
You are given three integers x,y and n. Your task is to find the maximum integer k such that 0≤k≤n
that k mod x = y, where mod is modulo operation. Many programming languages use percent operator 
% to implement it.

In other words, with given x, y and n you need to find the maximum possible integer from 0
to n that has the remainder y modulo x.

You have to answer t independent test cases. It is guaranteed that such k
exists for each test case.

Input
=====
The first line of the input contains one integer t (1≤t≤5⋅10^4) — the number of test cases. 
The next t lines contain test cases.

The only line of the test case contains three integers x,y and n (2≤x≤109; 0≤y<x; y≤n≤109).

It can be shown that such k always exists under the given constraints.

Output
======
For each test case, print the answer — maximum non-negative integer k such that 0≤k≤n 
and kmodx=y. It is guaranteed that the answer always exists.

k mod 7 = 5
k=qx+y

k = remainder * x + y
k = 7*5 + 5
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
    x, y, n = getIntList()

    maxvalue = y + (n - y) // x * x

    print(maxvalue)


