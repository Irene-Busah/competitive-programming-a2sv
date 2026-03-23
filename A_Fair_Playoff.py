"""
Four players participate in the playoff tournament. The tournament is held according to the 
following scheme: the first player will play with the second, and the third player with the 
fourth, then the winners of the pairs will play in the finals of the tournament.

It is known that in a match between two players, the one whose skill is greater will win. 
The skill of the t-th player is equal to si and all skill levels are pairwise different 
(i.e. there are no two identical values in the array s).

The tournament is called fair if the two players with the highest skills meet in the finals.

Determine whether the given tournament is fair.

Input
=====
The first line contains a single integer t (1≤t≤10^4) — the number of test cases.

A single line of test case contains four integers s1,s2,s3,s4 (1≤si≤100) — skill of the 
players. It is guaranteed that all the numbers in the array are different.

Output
======
For each testcase, output YES if the tournament is fair, or NO otherwise.
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
    s1, s2, s3, s4 = getIntList()

    finals = []
    lose = []

    if s1 > s2:
        finals.append(s1)
        lose.append(s2)
    else:
        finals.append(s2)
        lose.append(s1)
    
    if s3 > s4:
        finals.append(s3)
        lose.append(s4)
    else:
        finals.append(s4)
        lose.append(s3)

    possible = True
    for i in range(len(finals)):
        if min(finals) < lose[i]:
            # print(min(finals))
            possible = False
    
    if possible:
        print("YES")
    else:
        print("NO")
    
    # print(finals)



