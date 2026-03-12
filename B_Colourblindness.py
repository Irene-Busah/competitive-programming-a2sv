"""
Vasya has a grid with 2 rows and n columns. He colours each cell red, green, or blue.

Vasya is colourblind and can't distinguish green from blue. Determine if Vasya will consider the 
two rows of the grid to be coloured the same.

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — 
the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤100) — the number of columns of the grid.

The following two lines each contain a string consisting of n characters, each of which is either 
R, G, or B, representing a red, green, or blue cell, respectively — the description of the grid.

Output
For each test case, output "YES" if Vasya considers the grid's two rows to be identical, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    cols = getInt()

    colors1 = list(getStr().split())
    colors2 = list(getStr().split())


    matrix = [colors1, colors2]

    print(matrix)
    




