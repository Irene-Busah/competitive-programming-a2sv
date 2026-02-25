"""
A ticket is a string consisting of six digits. A ticket is considered lucky if the sum of the 
first three digits is equal to the sum of the last three digits. Given a ticket, output if 
it is lucky or not. Note that a ticket can have leading zeroes.

Input
=====
The first line of the input contains an integer t (1≤t≤10^3) — the number of testcases.

The description of each test consists of one line containing one string consisting of six digits.

Output
======
Output t lines, each of which contains the answer to the corresponding test case. Output "YES" 
if the given ticket is lucky, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" 
will be recognized as a positive answer).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting input data
numOfTestCases = getInt()


for _ in range(numOfTestCases):
    ticket = getStr()

    ticket = [int(x) for x in ticket]

    # print(ticket)

    # print(ticket[3:], ticket[:-3])

    if sum(ticket[3:]) == sum(ticket[:-3]):
        print("YES")
    else:
        print("NO")

