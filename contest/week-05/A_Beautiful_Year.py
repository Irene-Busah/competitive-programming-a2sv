"""
It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 
is the first year after the old 1987 with only distinct digits.

Now you are suggested to solve the following problem: given a year number, 
find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input
The single line contains integer y (1000≤y≤9000) — the year number.

Output
Print a single integer — the minimum year number that is strictly larger than y and 
all it's digits are distinct. It is guaranteed that the answer exists.

"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the year
year = getInt()

year += 1

while len(set(str(year))) != 4:
    year += 1

print(year)

