"""
You are given 4 sticks of lengths a, b, c, and d. You can not break or bend them.

Determine whether it is possible to form a square* using the given sticks.


A square is defined as a polygon consisting of 4 vertices, of which all sides have 
equal length and all inner angles are equal. No two edges of the polygon may 
intersect each other.

Input
======
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The only line of each test case contains four integers a, b, c, and d(1≤a,b,c,d≤10) 
— the lengths of the sticks.

Output
=======
For each test case, print "YES" if it is possible to form a square using the given 
sticks, and "NO" otherwise.

You may print each letter in any case (uppercase or lowercase). 
For example, the strings "yEs", "yes", "Yes", and "YES" will all be recognized 
as a positive answer.
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



# getting the number of test cases
numOfTestCases = getInt()

# going through each test case
for _ in range(numOfTestCases):
    sticksLens = getIntList()

    s1, s2, s3, s4 = sticksLens

    if s1 == s2 == s3 == s4:
        print("YES")
    else:
        print("NO")




