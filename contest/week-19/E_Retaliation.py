"""
Yousef wants to explode an array 𝑎1,𝑎2,…,𝑎𝑛
. An array gets exploded when all of its elements become equal to zero.

In one operation, Yousef can do exactly one of the following:

For every index 𝑖
 in 𝑎
, decrease 𝑎𝑖
 by 𝑖
.
For every index 𝑖
 in 𝑎
, decrease 𝑎𝑖
 by 𝑛−𝑖+1
.
Your task is to help Yousef determine if it is possible to explode the array using any number of operations.

Input
The first line of the input contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains an integer 𝑛
 (2≤𝑛≤2⋅105
) — the size of the array.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the elements of the array.

It is guaranteed that the sum of 𝑛
 over all test cases doesn't exceed 2⋅105
.

Output
For each test case, print "YES" if Yousef can explode the array, otherwise output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
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
    n = int(input())
    a = list(map(int, input().split()))
    
    # check arithmetic progression
    d = a[1] - a[0]
    ok = True
    for i in range(2, n):
        if a[i] - a[i-1] != d:
            ok = False
            break
    
    if not ok:
        print("NO")
        continue
    
    # solve for x, y
    numerator = n * a[0] - a[-1]
    denominator = n * n - 1
    
    if numerator % denominator != 0:
        print("NO")
        continue
    
    y = numerator // denominator
    x = a[0] - y * n
    
    if x >= 0 and y >= 0:
        print("YES")
    else:
        print("NO")

