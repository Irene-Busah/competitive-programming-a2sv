"""
Little girl Tanya is learning how to decrease a number by one, but she does it 
wrong with a number consisting of two or more digits. Tanya subtracts one from a 
number by the following algorithm:

    - if the last digit of the number is non-zero, she decreases the number by one;
    - if the last digit of the number is zero, she divides the number by 10 (i.e. 
    removes the last digit).
You are given an integer number n. Tanya will subtract one from it k times. 
Your task is to print the result after all k subtractions.

It is guaranteed that the result will be positive integer number.

Input
The first line of the input contains two integer numbers n and k (2≤n≤10^9, 1≤k≤50) — 
the number from which Tanya will subtract and the number of subtractions correspondingly.

Output
Print one integer number — the result of the decreasing n by one k times.

It is guaranteed that the result will be positive integer number.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the input data
num, k = getIntSeq()



for i in range(k):
    if num % 10 != 0:
        num -= 1
    else:
        num = int(num / 10)

print(num)
    


