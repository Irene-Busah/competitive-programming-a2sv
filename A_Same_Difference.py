"""
You are given a string s of length n, consisting of lowercase letters.

In one operation, you can select an integer i such that 1≤i<n
and change si into si+1


What is the minimum number of operations needed to make every character the same? 
It can be proved that this is always possible.

Input
=====
Each test contains multiple test cases. The first line contains the number of test 
cases t (1≤t≤20). The description of the test cases follows.

The first line of each test case contains an integer n (2≤n≤100) — 
the length of the string.

The following line contains a string s of length n, consisting of lowercase letters.

It is guaranteed that the sum of n over all test cases does not exceed 100.

Output
For each test case, output a single integer — the minimum number of operations needed
to make every character the same.

eest
esst
estt
sstt
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



# getting the number of test cases
numOfTestCases = getInt()

# getting each test cases
for _ in range(numOfTestCases):
    lenString = getInt()

    word = list(getStr())

    min_moves = 0
    target = word[-1]

    for i in range(lenString-1):
        if word[i] != target:
            min_moves += 1

    print(min_moves)


