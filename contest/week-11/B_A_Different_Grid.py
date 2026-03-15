"""
Alice was organizing numbered cards on a board 𝑎
. The board has 𝑛
 rows and 𝑚
 columns, containing all numbers from 1
 to 𝑛⋅𝑚
. The number in the 𝑖
-th row and 𝑗
-th column is denoted by 𝑎𝑖,𝑗
.

After looking at the arrangement, Alice decided she wanted a completely different placement of the cards. She plans to create another board 𝑏
 with the same dimensions 𝑛×𝑚
, which will also contain all integers from 1
 to 𝑛⋅𝑚
, but with one rule:

For every cell (𝑖,𝑗)
, the number in the new board must be different from the number originally there. In other words, 𝑎𝑖,𝑗≠𝑏𝑖,𝑗for all 1≤𝑖≤𝑛,1≤𝑗≤𝑚
.

Your task is to construct any valid board 𝑏
 that satisfies this condition, or determine that it is impossible.

Input
Each test consists of multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤103
) — the number of test cases.

The first line of each test case contains two integers 𝑛
 and 𝑚
 (1≤𝑛,𝑚≤10
) — the number of rows and columns of the board 𝑎
.

The next 𝑛
 lines contain 𝑚
 integers each, describing the board 𝑎
. The 𝑗
-th number in the 𝑖
-th row represents 𝑎𝑖,𝑗
.

It is guaranteed that all numbers in board 𝑎
 are distinct and 1≤𝑎𝑖,𝑗≤𝑛⋅𝑚
.

It is guaranteed that the sum of 𝑛⋅𝑚
 over all test cases does not exceed 5⋅104
.

Output
For each test case, output 𝑛⋅𝑚
 integers — any suitable board 𝑏
, or −1
 if such a board does not exist.
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
    n, m = getIntList()

    board = [getIntList() for _ in range(n)]

    if n*m == 1:
        print(-1)
        continue

    new_board = []

    for row in board:
        new_board.extend(row)
    
    shiftedArray = new_board[1:] + new_board[:1]

    indx = 0
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(shiftedArray[indx])
            indx += 1
        print(*new_row)



