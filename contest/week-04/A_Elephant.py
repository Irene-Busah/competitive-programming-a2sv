"""
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 
and his friend's house is located at point x(x>0) of the coordinate line. In one step the elephant 
can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to 
make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1≤x≤1000000) — The coordinate of the friend's house.

Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x.
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
friendCoordinate = getInt()


moves = (friendCoordinate + 4) // 5




print(moves)