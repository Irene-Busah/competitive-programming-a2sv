"""
Leo has developed a new programming language C+=. In C+=, integer variables can only be changed 
with a "+=" operation that adds the right-hand side value to the left-hand side variable. 
For example, performing "a += b" when a = 2, b = 3 changes the value of a to 5 (the value 
of b does not change).

In a prototype program Leo has two integer variables a and b, initialized with some positive 
values. He can perform any number of operations "a += b" or "b += a". Leo wants to test handling 
large integers, so he wants to make the value of either a or b strictly greater than a given 
value 𝑛. What is the smallest number of operations he has to perform?

Input
The first line contains a single integer 𝑇 (1≤𝑇≤100) — the number of test cases.

Each of the following 𝑇 lines describes a single test case, and contains three 
integers 𝑎,𝑏,𝑛 (1≤𝑎,𝑏≤𝑛≤109) — initial values of a and b, and the value one of the 
variables has to exceed, respectively.

Output
For each test case print a single integer — the smallest number of operations needed. Separate 
answers with line breaks.
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
    a, b, n = getIntList()

    count = 0

    while max(a, b) <= n:
        if a < b:
            a += b
        else:
            b += a
        count += 1
    
    print(count)
