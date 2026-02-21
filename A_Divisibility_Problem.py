"""
You are given two positive integers a and b. In one move you can increase a by 1 (replace a 
with a+1). Your task is to find the minimum number of moves you need to do in order to make a
divisible by b. It is possible, that you have to make 0 moves, as a is already divisible by b.
You have to answer t independent test cases.

Input
=====
The first line of the input contains one integer t (1≤t≤104) — the number of test cases. Then t
 test cases follow.

The only line of the test case contains two integers a and b (1≤a,b≤10^9).

Output
For each test case print the answer — the minimum number of moves you need to do in 
order to make a divisible by b.
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of inputs
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    a, b = getIntSeq()

    if a % b == 0:
        print(0)
    else:
        print(b - (a % b))

