"""
Valera the Horse is going to the party with friends. He has been following the fashion trends for a while, and he knows that 
it is very popular to wear all horseshoes of different color. Valera has got four horseshoes left from the last year, 
but maybe some of them have the same color. In this case he needs to go to the store and buy some few more horseshoes, 
not to lose face in front of his stylish comrades.

Fortunately, the store sells horseshoes of all colors under the sun and Valera has enough money to buy any 
four of them. However, in order to save the money, he would like to spend as little money as possible, so you 
need to help Valera and determine what is the minimum number of horseshoes he needs to buy to wear four horseshoes 
of different colors to a party.

Input
The first line contains four space-separated integers s1,s2,s3,s4 (1≤s1,s2,s3,s4≤109) — the colors of horseshoes Valera has.

Consider all possible colors indexed with integers.

Output
Print a single integer — the minimum number of horseshoes Valera needs to buy.
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



shoeColors = getIntList()


counter = set(shoeColors)

minColorsNeeded = len(shoeColors) - len(counter)

# for i in range(len(shoeColors)):

# for key in counter.keys():
#     if counter[key] >= 2:
#         minColorsNeeded += 1

print(minColorsNeeded)


