"""
Suneet has three digits a, b, and c.

Since math isn't his strongest point, he asks you to determine if you can choose any two digits to make a sum greater or equal to 10


Output "YES" if there is such a pair, and "NO" otherwise.

Input
=====
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The only line of each test case contains three digits a, b, c (0≤a,b,c≤9).

Output
For each test case, output "YES" if such a pair exists, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of test case
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    array = getIntList()

    # soring the array
    array.sort()

    # for i in range(len(array)):
    target = sum(array[1:])

    # print(array[1:], target)

    if target >= 10:
        print("YES")
    else:
        print("NO")

