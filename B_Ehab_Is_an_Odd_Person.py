"""
You're given an array a of length n. You can perform the following operation on it as many times as you want:

Pick two integers i and j (1≤i,𝑗≤𝑛) such that ai+aj is odd, then swap ai and aj

What is lexicographically the smallest array you can obtain?

An array 𝑥
 is lexicographically smaller than an array 𝑦
 if there exists an index 𝑖
 such that 𝑥𝑖<𝑦𝑖
, and 𝑥𝑗=𝑦𝑗
 for all 1≤𝑗<𝑖
. Less formally, at the first index 𝑖
 in which they differ, 𝑥𝑖<𝑦𝑖

Input
The first line contains an integer 𝑛
 (1≤𝑛≤105
) — the number of elements in the array 𝑎
.

The second line contains 𝑛
 space-separated integers 𝑎1
, 𝑎2
, …
, 𝑎𝑛
 (1≤𝑎𝑖≤109
) — the elements of the array 𝑎
.

Output
The only line contains 𝑛
 space-separated integers, the lexicographically smallest array you can obtain.
"""



import sys

# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the length of the array
lengthOfArray = getInt()

array = getIntList()
has_odd = any(x % 2 == 1 for x in array)
has_even = any(x % 2 == 0 for x in array)

if has_even and has_odd:
    array.sort()

print(*array)



