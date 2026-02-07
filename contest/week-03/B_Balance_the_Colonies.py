"""
A large-scale simulation is being conducted with 𝑛
 participants. Before the simulation begins, all participants must be divided into small groups, where each group contains either 2 or 3 people. Every participant must belong to exactly one group.

After forming the groups, each group independently chooses one of two colonies to join: Colony A or Colony B. All members of a group always join the same colony.

The organizers want the two colonies to be as balanced as possible. Your task is to determine the minimum possible difference between the number of people in Colony A and Colony B, assuming the groups are formed optimally and assigned to colonies in the best possible way.

Input
Each test consists of several test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤104)
 — the number of test cases. The following lines describe the test cases.

In the only line of each test case, there is an integer 𝑛
 — the number of people participating in the simulation (2≤𝑛≤104)
.

Output
For each number 𝑛
, output the minimum possible difference between the number of participants assigned to the two colonies.
"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of test cases, t
numOfTestCases = getInt()


for _ in range(numOfTestCases):
    numOfParticipants = getInt()

    minNumOfParticant = 2
    maxNumOfParticant = 3

    if numOfParticipants == minNumOfParticant:
        print(minNumOfParticant)
    elif numOfParticipants == maxNumOfParticant:
        print(maxNumOfParticant)
    
    elif numOfParticipants >= 4 and numOfParticipants % 2 == 0:
        print(0)
    else:
        print(1)

    
