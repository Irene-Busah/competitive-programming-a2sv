"""
Let's call a positive integer composite if it has at least one divisor other than 1
 and itself. For example:

the following numbers are composite: 1024
, 4
, 6
, 9
;
the following numbers are not composite: 13
, 1
, 2
, 3
, 37
.
You are given a positive integer 𝑛
. Find two composite integers 𝑎,𝑏
 such that 𝑎−𝑏=𝑛
.

It can be proven that solution always exists.

Input
The input contains one integer 𝑛
 (1≤𝑛≤107
): the given integer.

Output
Print two composite integers 𝑎,𝑏
 (2≤𝑎,𝑏≤109,𝑎−𝑏=𝑛
).

It can be proven, that solution always exists.

If there are several possible solutions, you can print any.

"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


number = getInt()

def is_composite(x):
    if x <= 3:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return True
    return False



for b in [4, 6, 8, 9, 10]:
    a = number + b
    if is_composite(a):
        print(a, b)
        break

