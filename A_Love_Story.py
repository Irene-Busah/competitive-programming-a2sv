"""
Timur loves codeforces. That's why he has a string s having length 10
made containing only lowercase Latin letters. Timur wants to know how many indices string s
 differs from the string "codeforces".

For example string s="coolforsez" differs from "codeforces" in 4 indices, shown in bold.

Help Timur by finding the number of indices where string s differs from "codeforces".

Note that you can't reorder the characters in the string s


Input
The first line contains a single integer t (1≤t≤1000
) — the number of test cases.

Each test case is one line and contains the string s, consisting of exactly 10
lowercase Latin characters.

Output
For each test case, output a single integer — the number of indices where string s differs.

"""

import sys
from typing import Counter

# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestCases = getInt()
string = "codeforces"
# stringCounter = Counter(string)

for _ in range(numOfTestCases):
    word = getStr()

    counter = 0

    for k, v in enumerate(word):
        if string[k] != v:
            counter += 1

    print(counter)


