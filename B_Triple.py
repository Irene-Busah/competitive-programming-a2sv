"""
Given an array 𝑎
 of 𝑛
 elements, print any value that appears at least three times or print -1 if there is no such value.

Input
The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains an integer 𝑛
 (1≤𝑛≤2⋅105
) — the length of the array.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤𝑛
) — the elements of the array.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print any value that appears at least three times or print -1 if there is no such value.
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
    lenOfArray = getInt()

    array = getIntList()

    counter = {}

    ans = -1
    for num in array:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] == 3:
            ans = num
            # print(key)
            break

    print(ans)
    # print(counter)
