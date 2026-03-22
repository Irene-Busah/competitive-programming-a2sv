import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


n, m = getIntList()

left, right = 1, n

for _ in range(m):
    clue = getStr().split()

    i = int(clue[-1])

    if clue[2] == 'left':
        right = min(right, i - 1)
    else:
        left = max(left, i + 1)

if left > right:
    print(-1)
else:
    print(right - left + 1)



