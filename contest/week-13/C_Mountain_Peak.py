import sys

# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


t = getInt()

for _ in range(t):
    n = getInt()
    h = getIntList()

    # precompute right minimums
    right_min_val = [0] * n
    right_min_idx = [0] * n

    right_min_val[n - 1] = h[n - 1]
    right_min_idx[n - 1] = n - 1

    for i in range(n - 2, -1, -1):
        if h[i] < right_min_val[i + 1]:
            right_min_val[i] = h[i]
            right_min_idx[i] = i
        else:
            right_min_val[i] = right_min_val[i + 1]
            right_min_idx[i] = right_min_idx[i + 1]

    # scan with left minimum
    left_min_val = h[0]
    left_min_idx = 0

    found = False

    for j in range(1, n - 1):
        if left_min_val < h[j] and right_min_val[j + 1] < h[j]:
            print("YES")
            print(left_min_idx + 1, j + 1, right_min_idx[j + 1] + 1)
            found = True
            break

        if h[j] < left_min_val:
            left_min_val = h[j]
            left_min_idx = j

    if not found:
        print("NO")