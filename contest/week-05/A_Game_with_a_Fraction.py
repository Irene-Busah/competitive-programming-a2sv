"""
Alice and Bob have two integers p and q, and they are playing a game with these numbers. 
The players take turns, with Alice going first. On their turn, a player can do one of two actions:

- decrease p by one (this action is possible if p>0);
- decrease q by one (this action is possible if q>1).

The game ends when p=0 and q=1.

Bob wins if at any point during the game the fraction p/q is equal to in value the fraction 2/3. 
Otherwise, Alice wins.

Given the initial values of p and q, determine the winner of the game if both players play optimally.

Input
=====
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). 
The description of the test cases follows.

Each input case consists of a single line containing two integers p and q (1≤p,q≤1018).

Output
======
For each input case, output:
    - "Alice" if Alice wins;
    - "Bob" if Bob wins.
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
    p, q = getIntList()

    # If already 2/3 at start
    if 3 * p == 2 * q:
        print("Bob")
        continue

    kmax = min(p // 2, q // 3)

    if p < q and kmax >= (q - p):
        print("Bob")
    else:
        print("Alice")






