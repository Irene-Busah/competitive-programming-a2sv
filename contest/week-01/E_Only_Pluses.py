"""
Kmes has written three integers, a, b and c in order to remember that he has to 
give Noobish_Monk axbxc bananas.

Noobish_Monk has found these integers and decided to do the following at most 5 times:

- pick one of these integers;
- increase it by 1

For example, if a=2, b=3 and c=4, then one can increase a three times by one and 
increase b two times. After that a=5, b=5, c=4. Then the total number of bananas 
will be 5x5x5=100

What is the maximum value of axbxc Noobish_Monk can achieve with these operations?

Input
======
Each test contains multiple test cases. The first line of input contains a single 
integer t (1≤t≤1000) — the number of test cases. The description of the test cases 
follows.

The first and only line of each test case contains three integers a, b and c 
(1≤a,b,c≤10) — Kmes's integers.

Output
=======
For each test case, output a single integer — the maximum amount of bananas Noobish_Monk 
can get.
"""


import sys

def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())




