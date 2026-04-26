"""
You are given an array of 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
.

The value of an array is the sum of the maximums of each prefix of the array. More formally, the value of an array 𝑎
 is ∑𝑛𝑖=1max(𝑎1,…,𝑎𝑖)
. For example, the value of the array [1,2,1
] is max(1)+max(1,2)+max(1,2,1)=1+2+2=5
.

You can choose two indices 𝑖
 and 𝑗
 and swap elements 𝑎𝑖
 and 𝑎𝑗
; this operation can be applied at most one time.

Find the maximum possible value of the array 𝑎
 after at most one operation.

Input
The first line of the input contains a single integer 𝑡
 (1≤𝑡≤100
) — the number of test cases.

The first line of each test case contains a single integer 𝑛
 (2≤𝑛≤50
) — the length of the array 𝑎
.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤104
) — the array 𝑎
.

Output
For each test case, output the maximum possible value of the array 𝑎
 after the swap has been performed.
"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


def compute_value(arr):
    total = 0
    current_max = 0
    
    for x in arr:
        current_max = max(current_max, x)
        total += current_max
    
    return total


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n = getInt()

    array = getIntList()

    results = compute_value(array)

    for i in range(n):
        array[0], array[i] = array[i], array[0]

        results = max(results, compute_value(array))

        array[0], array[i] = array[i], array[0]

    print(results)
