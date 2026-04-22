"""
You are given a string 𝑠
. You can apply this operation to the string exactly once: choose index 𝑖
 and move character 𝑠𝑖
 to the beginning of the string (removing it at the old position). For example, if you apply the operation with index 𝑖=4
 to the string "abaacd" with numbering from 1
, you get the string "aabacd". What is the lexicographically minimal†
 string you can obtain by this operation?

†
A string 𝑎
 is lexicographically smaller than a string 𝑏
 of the same length if and only if the following holds:

in the first position where 𝑎
 and 𝑏
 differ, the string 𝑎
 has a letter that appears earlier in the alphabet than the corresponding letter in 𝑏
.
Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤105
) — the length of the string.

The second line of each test case contains the string 𝑠
 of length 𝑛
, consisting of lowercase English letters.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105
.

Output
For each test case, on a separate line print the lexicographically smallest string that can be obtained after applying the operation to the original string exactly once.
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
    n = getInt()
    string = getStr()
    
    # Start with the original string (not moving anything)
    best = string
    
    # Only consider moving characters at positions where s[i] < s[i-1]
    for i in range(1, n):
        if string[i] < string[i-1]:
            # This position is a candidate for moving
            candidate = string[i] + string[:i] + string[i+1:]
            # Keep the lexicographically smallest result
            if candidate < best:
                best = candidate
    
    print(best)
