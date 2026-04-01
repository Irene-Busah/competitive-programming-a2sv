"""
Aser The Conqueror has recently integrated 𝑛
 new warriors into his grand army. To maintain absolute control, he must assign each warrior a unique power rank from 1
 to 𝑛
. However, his advisors have flagged certain positions—marked as 𝟷
 in a sacred string 𝑠
—as belonging to "Ambitious Officers." Aser knows that if an Ambitious Officer ever becomes the most powerful member of any local battalion of size 𝑘
 or more, they might gain enough influence to attempt a coup. To secure his reign, he must arrange the ranks such that no Ambitious Officer is ever the highest-ranked individual in any battalion they are a part of.

Formally, you are given a binary string∗
 𝑠
 of length 𝑛
, and an integer 𝑘
.

Aser The Conqueror wants to construct a permutation†
 𝑝
 of length 𝑛
, so that for each 1≤𝑖≤𝑛
, where 𝑠𝑖=𝟷
, the following holds:

For each interval [𝑙,𝑟]
 (1≤𝑙≤𝑟≤𝑛
) whose length is at least 𝑘
 (i.e. 𝑟−𝑙+1≥𝑘
), if it covers position 𝑖
 (i.e. 𝑙≤𝑖≤𝑟
), then the maximum element among 𝑝𝑙,𝑝𝑙+1,…,𝑝𝑟
 is not 𝑝𝑖
.
Note that there are no such constraints on indices with 𝑠𝑖=𝟶
.

You have to find such a permutation, or determine that such permutations do not exist.
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

    string = getStr()

    # Check for impossible case
    max_consecutive_ones = 0
    current = 0
    for c in string:
        if c == '1':
            current += 1
            max_consecutive_ones = max(max_consecutive_ones, current)
        else:
            current = 0

    if max_consecutive_ones >= k:
        print("NO")
        continue

    # Construct permutation
    ans = [0] * n
    ambitious = []
    normal = []

    for i, c in enumerate(string):
        if c == '1':
            ambitious.append(i)
        else:
            normal.append(i)

    # Assign smallest ranks to ambitious
    rank = 1
    for i in ambitious:
        ans[i] = rank
        rank += 1

    # Assign remaining ranks to normal
    for i in normal:
        ans[i] = rank
        rank += 1

    print("YES")
    print(*ans)



