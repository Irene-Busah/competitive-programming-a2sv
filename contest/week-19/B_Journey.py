"""
Monocarp decided to embark on a long hiking journey.

He decided that on the first day he would walk a kilometers, on the second day he would 
walk b kilometers, on the third day he would walk c kilometers, on the fourth day, just 
like on the first, he would walk a kilometers, on the fifth day, just like on the second, 
he would walk b kilometers, on the sixth day, just like on the third, he would walk c kilometers, 
and so on.

Monocarp will complete his journey on the day when he has walked at least n kilometers 
in total. Your task is to determine the day on which Monocarp will complete his journey.

Input
=====
The first line contains one integer t (1<=t<=10^4) — the number of test cases.

Each test case consists of one line containing four integers n, a, b, c (1<=n<=10^9; 1<=a,b,c<=10^6).

Output
For each test case, output one integer — the day on which Monocarp will have walked 
at least 𝑛 kilometers in total and will complete his journey.
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
    n, a, b, c = getIntList()

    cycle = a + b + c
    
    cycles = n // cycle
    days = cycles * 3
    
    remaining = n - cycles * cycle
    
    if remaining > 0:
        days += 1
        remaining -= a
    
    if remaining > 0:
        days += 1
        remaining -= b
    
    if remaining > 0:
        days += 1
    
    print(days)


