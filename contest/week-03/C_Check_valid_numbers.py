"""
Raphael is obsessed with the concept of "The Harmonic Constraint." To him, an array isn't 
just a list of numbers; it's a rhythm that must be perfectly balanced. He believes that if 
every segment of a fixed length p sums to the exact same value q, the array achieves a state 
of "local resonance." However, he also needs the entire array of length n to sum to a total value 𝑚
to satisfy the "global equilibrium."

His friends think he's overcomplicating things, but Raphael is convinced that such arrays are the key 
to understanding the universe. Can you help him determine if his dream array actually exists, or if 
he's chasing a mathematical ghost?

Given four integers n, 𝑚, p, and q, determine whether there exists an integer array a1,a2,…,an
(elements may be negative) satisfying the following conditions:

The sum of all elements in the array is equal to 𝑚: a1+a2+…+an=𝑚
The sum of every p consecutive elements is equal to q :ai+ai+1+…+ai+p-1=q, for all 1≤i≤n-p+1


Input
======
Each test contains multiple test cases. The first line contains the number of test cases t
(1≤t≤10^4). The description of the test cases follows.

The first and only line of each test case contains four integers n, 𝑚, p, and q (1≤p≤n≤100, 1≤q,𝑚≤100) — 
the length of the array, the sum of elements, the length of a segment, and the sum of a segment, 
respectively.

Output
=======
For each test case, output "YES" (without quotes) if there exists an array satisfying the above conditions, 
and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes", and "Yes" will all be 
recognized as valid responses).

# n = 3
# m = 2
# p = 2
# q = 1

# [a1, a2, a3]

# a1 + a2 = 1
# a2 + a3 = 1
# a1 + a2 + a3 = 2


# m == k * q
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))



# getting the number of test cases, t
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    lengthOfEntireArray, sumOfEntireArr, segmentLength, sumOfSegLength = getIntList()

    k = lengthOfEntireArray // segmentLength

    if lengthOfEntireArray % segmentLength != 0:
        print('YES')
    else:
        print('YES' if sumOfEntireArr == k * sumOfSegLength else 'NO')



# n = 3
# m = 2
# p = 2
# q = 1

# a1, a2, a3

# a1 + a2 = 1
# a2 + a3 = 1
# a1 + a2 + a3 = 2


# m == k * q



