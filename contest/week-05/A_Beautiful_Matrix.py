"""
You've got a 5x5 matrix, consisting of 24 zeroes and a single number one. Let's index the 
matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by 
numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the 
two following transformations to the matrix:

1. Swap two neighboring matrix rows, that is, rows with indexes i and i+1 for some integer i (1≤i<5).
2. Swap two neighboring matrix columns, that is, columns with indexes j and j+1 for some 
integer j (1≤j<5).

You think that a matrix looks beautiful, if the single number one of the matrix is located 
in its middle (in the cell that is on the intersection of the third row and the third column). 
Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.
"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the matrix
matrix = [getIntList() for _ in range(5)]

mid_row = (len(matrix)) // 2
mid_col = (len(matrix)) // 2

row = 0
col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # if i == mid_row and j == mid_col:
        if matrix[i][j] == 1:
            row = abs(mid_row - i)
            col = abs(mid_col - j)
print(row + col)

# print(mid)


