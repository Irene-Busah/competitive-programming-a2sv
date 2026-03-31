"""
You are given a permutation† n of size n. You can do the following operation

Select an index t from 2 to n-1 such that ai-1<ai and ai>ai+1. Swap ai and ai+1.
Determine whether it is possible to sort the permutation after a finite number of operations.


A permutation is an array consisting of n distinct integers from 1 to n
in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2
appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
======
Each test contains multiple test cases. The first line contains the number of test cases t (1≤n≤5000). 
Description of the test cases follows.

The first line of each test case contains a single integer n (3≤n≤10) — the size of the permutation.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤n) — 
the elements of permutation a


Output
======
For each test case, print "YES" if it is possible to sort the permutation, and "NO" otherwise.

You may print each letter in any case (for example, "YES", "Yes", "yes", "yEs" will all be 
recognized as positive answer).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the input data
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n = getInt()
    a = getIntList()

    sorted_a = sorted(a)
    changed = True

    # Repeat until no swaps
    while changed:
        changed = False
        for i in range(1, n-1):
            if a[i-1] < a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                changed = True

    if a == sorted_a:
        print("YES")
    else:
        print("NO")




