"""
Tsedeniya is playing the hit rhythm game osu!. The game can be described by a binary string∗
 𝑠
 of length 𝑛
 and a positive integer 𝑘
 where the following will happen in order:

You will choose some positions in 𝑠
 to protect.
Then for each 𝑖
 (1≤𝑖≤𝑛
) in increasing order, Tsedeniya can set 𝑠𝑖
 to 𝟶
 if all the following are true:
𝑠𝑖=𝟷
,
𝑠𝑖
 is not protected,
the previous 𝑘−1
 elements do not contain 𝟷
. More formally, 𝟷
 does not occur in 𝑠max(1,𝑖−𝑘+1),…,𝑠𝑖−1
.
You want to challenge her and make her task difficult. So determine the minimum number of positions you need to protect to force her to leave 𝑠
 unchanged.

∗
A binary string is a string that only consists of characters 𝟶
 and 𝟷
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤100
). The description of the test cases follows.

The first line of each testcase contains integers 𝑛
 and 𝑘
 (2≤𝑛≤1000
; 2≤𝑘≤𝑛
) — the length of 𝑠
 and 𝑘
.

The second line of each test case contains a binary string 𝑠
 of length 𝑛
 consisting of characters 𝟶
 and 𝟷
.

The sum of 𝑛
 across all testcases does not exceed 1000
.

Output
For each testcase, output the minimum number of positions you need to protect to force Tsedeniya to leave the string unchanged.
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

    count = 0
    last_1 = -k  # index of last 1 that is considered “covering” a window

    for i in range(n):
        if s[i] == '1':
            if i - last_1 >= k:
                count += 1  # must protect
            last_1 = i  # update last 1

    print(count)




