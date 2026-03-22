"""
You are given a string 𝑠
 that only consists of 0 and 1 of length 𝑛
. The 𝑖
-th character of 𝑠
 is denoted as 𝑠𝑖
, where 1≤𝑖≤𝑛
. You are allowed to perform the following operation on the string 𝑠
 exactly once:

Choose a segment [𝑙,𝑟]
 (1≤𝑙≤𝑟≤𝑛
). For 𝑙≤𝑖≤𝑟
, change 𝑠𝑖
 into 1 if 𝑠𝑖
 is 0, and change 𝑠𝑖
 into 0 if 𝑠𝑖
 is 1.
For example, let 𝑠
 be 010100 and the segment [2,5]
 is chosen. The string 𝑠
 will be 001010 after performing the operation. Determine whether it is possible to make 𝑠
 a palindrome after performing the operation exactly once. A string is a palindrome iff it reads the same backwards as forwards. For example, 010010 is a palindrome but 10111 is not.
Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows. The first line of each test case contains a single integer 𝑛
 (2≤𝑛≤105
) — the length of string 𝑠
. The second line of each test case contains a binary string 𝑠
 of length 𝑛
. Only characters 0 and 1 can appear in 𝑠
. It's guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print Yes if 𝑠
 can be a palindrome after performing the operation exactly once, and print No if not. You can output Yes and No in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).


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
    lenOfString = getInt()

    string = [s for s in getStr()]

    mismatchIndex = []

    # left, right = 0, lenOfString - 1

    # while left <= right:
    #     if string[le]

    for i in range(lenOfString//2):
        if string[i] != string[lenOfString - 1 - i]:
            mismatchIndex.append(i)
    
    if not mismatchIndex:
        print("Yes")
        continue
    
    possible = True
    for i in range(1, len(mismatchIndex)):
        if mismatchIndex[i] != mismatchIndex[i - 1] + 1:
            possible = False
            break
    
    if possible:
        print("Yes")
    else:
        print("No")


