import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


n = getInt()
nums = getIntList()

max_val = max(nums)
min_val = min(nums)

# leftmost max
max_idx = nums.index(max_val)

# rightmost min
min_idx = len(nums) - 1 - nums[::-1].index(min_val)

moves = max_idx + (n - 1 - min_idx)

if min_idx < max_idx:
    moves -= 1

print(moves)

