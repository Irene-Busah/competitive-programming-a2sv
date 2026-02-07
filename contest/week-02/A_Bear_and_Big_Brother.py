"""
Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller 
than or equal to his brother's weight.

Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every 
year.

After how many full years will Limak become strictly larger (strictly heavier) than Bob?

Input
======
The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Limak and the 
weight of Bob respectively.

Output
======
Print one integer, denoting the integer number of years after which Limak will become strictly larger 
than Bob.

Example
=======
Input: [4, 7]
Output: 2
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


limakWeight, bobWeight = getIntList()
years = 0

while limakWeight <= bobWeight:
    limakWeight = 3 * limakWeight
    bobWeight = 2 * bobWeight

    years += 1

print(years)






