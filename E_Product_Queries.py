"""
Today, Sabyrzhan was called to the board with an array a of length n
and was assigned an officer's task — to answer n questions.

In the i-th question, it is required to determine the minimum number of elements 
from the array that need to be selected from the board (it is allowed to use the 
same element multiple times) so that their product is exactly equal to i, 
or to report that it is impossible to achieve such a product.

Note that at least one element must be selected.

Input
======
Each test consists of several test cases. The first line contains one integer t (1≤t≤10^4) — 
the number of test cases. The description of the test cases follows.

The first line of each test case contains one integer n(1≤n≤3⋅10^5).

The second line of each test case contains n integers a1,a2,…,an(1≤ai≤n).

It is guaranteed that the sum of the values of n across all test cases does not exceed 3⋅10^5.

Output
=======
For the i-th question, output one integer — the minimum number of elements from the array required 
to obtain a product equal to i, or -1 if it is impossible to achieve such a product.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# number of test cases
# numOfTestCases = getInt()

INF = 10**9

t = getInt()
out_lines = []

for _ in range(t):
    n = getInt()
    arr = getIntList()

    present = [False] * (n + 1)
    for x in arr:
        present[x] = True

    dp = [INF] * (n + 1)
    dp[1] = 0  # helper state: product 1 with 0 picks

    # For each allowed factor x, update all multiples m = x, 2x, 3x, ...
    for x in range(2, n + 1):          # start at 2 (skip 1)
        if not present[x]:
            continue
        for m in range(x, n + 1, x):
            prev = m // x
            if dp[prev] != INF:
                cand = dp[prev] + 1
                if cand < dp[m]:
                    dp[m] = cand

    ans = []
    # i = 1 special: must pick at least one element
    ans.append("1" if present[1] else "-1")
    for i in range(2, n + 1):
        ans.append("-1" if dp[i] == INF else str(dp[i]))

    out_lines.append(" ".join(ans))

sys.stdout.write("\n".join(out_lines))

