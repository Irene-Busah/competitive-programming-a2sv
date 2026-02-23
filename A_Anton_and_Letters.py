"""
Recently, Anton has found a set. The set consists of small English letters. Anton carefully wrote out all the 
letters from the set in one line, separated by a comma. He also added an opening curved bracket at the 
beginning of the line and a closing curved bracket at the end of the line.

Unfortunately, from time to time Anton would forget writing some letter and write it again. 
He asks you to count the total number of distinct letters in his set.

Input
The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. 
It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. 
Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.

Output
Print a single number — the number of distinct letters in Anton's set.
"""


import sys

# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



data = getStr()

strSet = [x.strip('') for x in data if x.isalpha()]

counter = []

for x in strSet:
    if x not in counter:
        counter.append(x)

print(len(counter))



