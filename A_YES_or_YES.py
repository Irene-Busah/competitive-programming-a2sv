"""
There is a string s of length 3, consisting of uppercase and lowercase English letters. 
Check if it is equal to "YES" (without quotes), where each letter can be in any case. 
For example, "yES", "Yes", "yes" are all allowable.

Input
The first line of the input contains an integer t (1≤t≤10^3) — the number of testcases.

The description of each test consists of one line containing one string s consisting of 
three characters. Each character of s is either an uppercase or lowercase English letter.

Output
For each test case, output "YES" (without quotes) if s satisfies the condition, and "NO" 
(without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" 
will be recognized as a positive response).
"""

# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# reading the number of test cases
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    word = getStr()

    if word.upper() == 'YES' or word.lower() == 'yes':
        print("YES")
    else:
        print("NO")


