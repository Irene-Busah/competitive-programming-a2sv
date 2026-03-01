"""
Given a lowercase Latin character (letter), check if it appears in the string 𝚌𝚘𝚍𝚎𝚏𝚘𝚛𝚌𝚎𝚜.

Input
The first line of the input contains an integer t (1≤t≤26) — the number of test cases.

The only line of each test case contains a character c — a single lowercase Latin character (letter).

Output
For each test case, output "YES" (without quotes) if c satisfies the condition, and "NO" (without quotes) otherwise.

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



# getting the number of test cases
numOfTestCases = getInt()

word = list('codeforces')

for _ in range(numOfTestCases):
    char = getStr()

    # print(char)

    if char in word:
        print("YES")
    else:
        print("NO")

# print(word)

