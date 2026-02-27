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
    n, m = getIntList()

    array = getIntList()

    maxValue = max(array)

    ans = []

    for _ in range(m):
        op, l, r = getStrList()

        if int(l) <= maxValue <= int(r):
            if op == '+':
                maxValue += 1
            else:
                maxValue -= 1

        ans.append(str(maxValue))
    
    print(" ".join(ans))
