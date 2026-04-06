"""
You are given an array 𝑎[0…𝑛−1] of 𝑛 integers. This array is called a "valley" if 
there exists exactly one subarray 𝑎[𝑙…𝑟] such that:

1. 0 ≤ 𝑙 ≤ 𝑟 ≤ 𝑛 − 1

2. 𝑎𝑙 = 𝑎𝑙 + 1 = 𝑎𝑙 + 2 = ⋯ = 𝑎𝑟

3. 𝑙=0 or 𝑎𝑙−1>𝑎𝑙

4. 𝑟=𝑛−1 or 𝑎𝑟<𝑎𝑟+1

Here are three examples:


The first image shows the array [3,2,2,1,2,2,3], it is a valley because only subarray with 
indices 𝑙=𝑟=3 satisfies the condition.

The second image shows the array [1,1,1,2,3,3,4,5,6,6,6], it is a valley because only subarray 
with indices 𝑙=0,𝑟=2 satisfies the codition.

The third image shows the array [1,2,3,4,3,2,1], it is not a valley because two subarrays 
𝑙=𝑟=0 and 𝑙=𝑟=6 that satisfy the condition.

You are asked whether the given array is a valley or not.

Note that we consider the array to be indexed from 0


Input
=====
The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤2⋅105) — the length 
of the array.

The second line of each test case contains 𝑛 integers 𝑎𝑖 (1≤𝑎𝑖≤109) — the elements of the array.

It is guaranteed that the sum of 𝑛 over all test cases is smaller than 2⋅105.

Output
=======
For each test case, output "YES" (without quotes) if the array is a valley, and "NO" 
(without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and 
"YES" will be recognized as a positive answer).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestcases = getInt()


