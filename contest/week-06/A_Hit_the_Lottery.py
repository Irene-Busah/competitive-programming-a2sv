"""
Allen has a LOT of money. He has n dollars in the bank. For security reasons, he wants to withdraw 
it in cash (we will not disclose the reasons here). The denominations for dollar bills are 1, 5, 10, 20,
100. What is the minimum number of bills Allen could receive after withdrawing his entire balance?

Input
The first and only line of input contains a single integer n (1≤n≤109).

Output
Output the minimum number of bills that Allen could receive.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


notes = [100, 20, 10, 5, 1]


# getting the balance
money = getInt()

count = 0

for note in notes:
    count += money // note
    money %= note

print(count)


