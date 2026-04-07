"""
You have a stripe of checkered paper of length 𝑛. Each cell is either white or black.

What is the minimum number of cells that must be recolored from white to black in 
order to have a segment of 𝑘 consecutive black cells on the stripe?

If the input data is such that a segment of 𝑘 consecutive black cells already exists, 
then print 0.

Input
=====
The first line contains an integer 𝑡 (1≤𝑡≤104) — the number of test cases.

Next, descriptions of 𝑡 test cases follow.

The first line of the input contains two integers 𝑛 and 𝑘 (1≤𝑘≤𝑛≤2⋅105). The second line 
consists of the letters 'W' (white) and 'B' (black). The line length is 𝑛.

It is guaranteed that the sum of values 𝑛 does not exceed 2⋅105.

Output
======
For each of 𝑡 test cases print an integer — the minimum number of cells that need to be repainted 
from white to black in order to have a segment of 𝑘 consecutive black cells.
"""



import sys

def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n, k = getIntList()

    letters = getStr()

    """
    5 3
    BBWBW


    """

    whiteCounter = 0

    i = 0

    while i < n:
        pass

