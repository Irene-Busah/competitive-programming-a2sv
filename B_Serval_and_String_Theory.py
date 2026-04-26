"""

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
    n, k = getIntList()
    s = getStr()
    
    if s < s[::-1]:
        print("YES")
    elif k == 0:
        print("NO")
    elif len(set(s)) == 1:
        print("NO")
    else:
        print("YES")
