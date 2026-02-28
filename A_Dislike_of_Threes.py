"""
Polycarp doesn't like integers that are divisible by 3 or end with the digit 3
in their decimal representation. Integers that meet both conditions are disliked by Polycarp, too.

Polycarp starts to write out the positive (greater than 0) integers which he likes: 1,2,4,5,7,8,10,11,14,16,…
. Output the i-th element of this sequence (the elements are numbered from 1).

Input
The first line contains one integer t (1≤t≤100) — the number of test cases. Then t test cases follow.

Each test case consists of one line containing one integer k (1≤k≤1000).

Output
For each test case, output in a separate line one integer x — the k-th element of the sequence that was written out by Polycarp.
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



numOfTestCases = getInt()

for _ in range(numOfTestCases):
    k = int(input())

    count = 0
    num = 1

    while True:
        if num % 3 != 0 and num % 10 != 3:
            count += 1
            if count == k:
                print(num)
                break
        num += 1



