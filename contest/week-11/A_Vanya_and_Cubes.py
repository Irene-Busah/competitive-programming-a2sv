"""
Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as 
follows: the top level of the pyramid must consist of 1 cube, the second level must consist 
of 1+2=3 cubes, the third level must have 1+2+3=6 cubes, and so on. Thus, the i-th 
level of the pyramid must have 1+2+...+(i-1)+i cubes.

Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.

Input
The first line contains integer n (1≤n≤104) — the number of cubes given to Vanya.

Output
Print the maximum possible height of the pyramid in the single line.
"""



# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# reading the dat
cubes = getInt()

height = 0
level = 1

levelCubes = 0

while cubes >= level + levelCubes:
    levelCubes += level

    cubes -= levelCubes

    height += 1
    level += 1
    

print(height)
