"""
Raphael is obsessed with the concept of "The Harmonic Constraint." To him, an array isn't just a list of numbers; it's a rhythm that must be perfectly balanced. He believes that if every segment of a fixed length 𝑝
 sums to the exact same value 𝑞
, the array achieves a state of "local resonance." However, he also needs the entire array of length 𝑛
 to sum to a total value 𝑚
 to satisfy the "global equilibrium."

His friends think he’s overcomplicating things, but Raphael is convinced that such arrays are the key to understanding the universe. Can you help him determine if his dream array actually exists, or if he's chasing a mathematical ghost?

Given four integers 𝑛
, 𝑚
, 𝑝
, and 𝑞
, determine whether there exists an integer array 𝑎1,𝑎2,…,𝑎𝑛
 (elements may be negative) satisfying the following conditions:

The sum of all elements in the array is equal to 𝑚
:
𝑎1+𝑎2+…+𝑎𝑛=𝑚
The sum of every 𝑝
 consecutive elements is equal to 𝑞
:
𝑎𝑖+𝑎𝑖+1+…+𝑎𝑖+𝑝−1=𝑞, for all 1≤𝑖≤𝑛−𝑝+1
Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first and only line of each test case contains four integers 𝑛
, 𝑚
, 𝑝
, and 𝑞
 (1≤𝑝≤𝑛≤100
, 1≤𝑞,𝑚≤100
) — the length of the array, the sum of elements, the length of a segment, and the sum of a segment, respectively.

Output
For each test case, output "YES" (without quotes) if there exists an array satisfying the above conditions, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes", and "Yes" will all be recognized as valid responses).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of test cases, t
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    lengthOfEntireArray, sumOfEntireArr, segmentLength, sumOfSegLength = getIntList()

    k = lengthOfEntireArray // segmentLength

    if lengthOfEntireArray % segmentLength != 0:
        print('YES')
    else:
        print('YES' if sumOfEntireArr == k * sumOfSegLength else 'NO')



