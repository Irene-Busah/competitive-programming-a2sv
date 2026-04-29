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
    n, c = getStrList()
    n = int(n)
    s = getStr()
    
    if c == 'g':
        print(0)
        continue
    
    t_s = s + s
    next_g = float('inf')
    ans = 0
    
    # go from right to left
    for i in range(2*n - 1, -1, -1):
        if t_s[i] == 'g':
            next_g = i
        if i < n and s[i] == c:
            ans = max(ans, next_g - i)
    
    print(ans)

