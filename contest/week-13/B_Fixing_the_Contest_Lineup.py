"""
A contest consists of 𝑛
 problems. The difficulty of the 𝑖
-th problem is expected to be at most 𝑏𝑖
. Currently, there are 𝑛
 proposed problems, where the difficulty of the 𝑖
-th problem is 𝑎𝑖
.

Initially, both 𝑎1,𝑎2,…,𝑎𝑛
 and 𝑏1,𝑏2,…,𝑏𝑛
 are sorted in non-decreasing order.

Some problems may exceed their expected difficulty, so additional problems can be proposed. When a new problem with difficulty 𝑤
 is added, the following process occurs:

Insert 𝑤
 into the array 𝑎
.
Sort the array 𝑎
 in non-decreasing order.
Remove the last element from the array.
In other words, after each operation, the array 𝑎
 still contains exactly 𝑛
 elements.

Find the minimum number of operations required so that 𝑎𝑖≤𝑏𝑖
 for all 𝑖
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤100
). The description of the test cases follows.

The first line of each test case contains only one positive integer 𝑛
 (1≤𝑛≤100
), representing the number of problems.

The second line of each test case contains an array 𝑎
 of length 𝑛
 (1≤𝑎1≤𝑎2≤⋯≤𝑎𝑛≤109
).

The third line of each test case contains an array 𝑏
 of length 𝑛
 (1≤𝑏1≤𝑏2≤⋯≤𝑏𝑛≤109
).

Output
For each test case, print a single integer — the minimum number of operations required.
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
    numOfProblems = getInt()

    a = getIntList()
    b = getIntList()

    operations = 0

    left, right = 0, 0
    while right < numOfProblems:
        if left < numOfProblems and a[left] <= b[right]:
            left += 1
        else:
            operations += 1
            
        right += 1

    print(operations)
        



