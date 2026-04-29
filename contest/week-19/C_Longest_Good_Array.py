"""
Today, Sakurako was studying arrays. An array 𝑎 of length 𝑛 is considered good if and only if:

the array 𝑎 is increasing, meaning 𝑎𝑖−1<𝑎𝑖 for all 2≤𝑖≤𝑛;
the differences between adjacent elements are increasing, meaning 𝑎𝑖−𝑎𝑖−1<𝑎𝑖+1−𝑎𝑖 for all 2≤𝑖<𝑛.

Sakurako has come up with boundaries l and r and wants to construct a good array of 
maximum length, where 𝑙≤𝑎𝑖≤𝑟 for all 𝑎𝑖


Help Sakurako find the maximum length of a good array for the given 𝑙 and 𝑟.

Input
The first line contains a single integer t (1≤𝑡≤104)  — the number of test cases.

The only line of each test case contains two integers l and r (1≤𝑙≤𝑟≤109).

Output
For each test case, output a single integer  — the length of the longest good array Sakurako 
can form given l and r.
"""


import math
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
    l, r = map(int, input().split())
    
    d = r - l
    
    k = int((1 + math.isqrt(1 + 8*d)) // 2)
    
    print(k)


