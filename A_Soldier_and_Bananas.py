"""
A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k 
dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?

Input
=====
The first line contains three positive integers k,n,w (1≤k, w≤1000, 0≤n≤109), the cost of the first banana, 
initial number of dollars the soldier has and number of bananas he wants.

Output
======
Output one integer — the amount of dollars that the soldier must borrow from his friend. 
If he doesn't have to borrow money, output 0.
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
costOfBanana, initialNumOfDollars, NumOfBananaNeeded = getIntList()

totalCost = 0

for i in range(1, NumOfBananaNeeded + 1):
    # getting the cost of each banana
    totalCost += i * costOfBanana

# computing the amount to borrow
borrowAmount = totalCost - initialNumOfDollars

print(max(0, borrowAmount))





