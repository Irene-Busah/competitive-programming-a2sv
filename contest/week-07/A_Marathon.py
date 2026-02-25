"""
You are given four distinct integers a, b, c, d.

Timur and three other people are running a marathon. The value a is the distance 
that Timur has run and b, c, d correspond to the distances the other three participants ran.

Output the number of participants in front of Timur.

Input
The first line contains a single integer t (1≤t≤10^4) — the number of test cases.

The description of each test case consists of four distinct integers a, b, c, d (0≤a,b,c,d≤10^4).

Output
For each test case, output a single integer — the number of participants in front of Timur.
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
    timurDist, *otherDistances = getIntList()

    count = 0

    for x in otherDistances:
        if x > timurDist:
            count += 1

    print(count)


