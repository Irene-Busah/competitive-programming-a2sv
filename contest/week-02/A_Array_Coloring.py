"""
You have n cards arranged in a row. The t-th card has the integer ai written on it. All integers are 
distinct.

You must color each card either red or blue such that the following conditions are satisfied:

- Any two adjacent cards in the row have different colors.
- If you rearrange the cards so that the numbers on them are in increasing order, 
any two adjacent cards in the new row must also have different colors.
- Determine if such a coloring exists.

Input
=====
Each test contains multiple test cases. The first line contains the number of test cases t(1≤t≤200). 

The description of the test cases follows.

The first line of each test case contains a single integer n (2≤n≤100) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤n).

It is guaranteed that all elements of a are distinct.

Output
======
For each test case, output "YES" if you can color the cards so that the conditions are satisfied, 
and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", 
and "YES" will be recognized as positive responses.
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


# getting the number of test cases, t
numOfTestCases = getInt()

for _ in range(numOfTestCases):

    # getting the length of the array, n
    lengthOfRow = getInt()

    # getting the card row
    cards = getIntList()

    # pairs: (value, original_index)
    pairs = [(cards[i], i) for i in range(lengthOfRow)]
    pairs.sort() 

    ok = True
    for i in range(lengthOfRow - 1):
        idx1 = pairs[i][1]
        idx2 = pairs[i + 1][1]

        # original indices must have opposite parity
        if (idx1 % 2) == (idx2 % 2):
            ok = False
            break

    print("YES" if ok else "NO")


