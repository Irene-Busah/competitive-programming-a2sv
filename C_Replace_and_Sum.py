"""
Today, KQ has an exam at the Grail Academy. A strict teacher gave a task that KQ could not solve. 
He was given two arrays a and b of length n. KQ is allowed to perform the following operations 
on the arrays:

    - Choose an index t (1≤t<n) and replace ai with ai+1.
    - Choose an index t (1≤t≤n) and replace ai with bi.
Now he has q queries. Each query is described by two numbers l and r. 
His task is to find the maximum value of the sum (ai+ai+1+al+2+⋯+ar) for each query, 
if he can perform any number of operations on any elements of the array. Since he 
is not skilled enough for this, he asks for your help.


Input
=====
Each test consists of several test cases. The first line contains one integer t (1≤t≤10^4) — 
the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n, q (1≤n,q≤2⋅105).

The second line of each test case contains n integers a1,a2,...,an (1≤ai≤10^4)

The third line of each test case contains n integers b1,b2,...,bn (1≤bi≤104)


The following q lines contain two integers l and r (1≤l≤r≤n)


It is guaranteed that the sum of the values of n and the sum of the values of q across all test 
cases do not exceed 2⋅10^5


Output
For each test case, output q numbers separated by spaces — the maximum values of the 
sums (al+al+1+al+2+⋯+ar)
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
    lenOfArray, numOfQueries = getIntSeq()

    array_A = getIntList()
    array_B = getIntList()

    l, r = getIntSeq()


    for i in range(array_A):
        pass


