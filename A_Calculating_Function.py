"""
For a positive integer n let's define a function f:

f(n) = -1+2-3+..+(-1)nn

Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1≤n≤10^15).

Output
Print f(n) in a single line.
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
n = int(input().strip())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)