"""
Polycarp has a favorite sequence a[1…n] consisting of n integers. He wrote it out on the 
whiteboard as follows:

- he wrote the number a1 to the left side (at the beginning of the whiteboard);
- he wrote the number a2 to the right side (at the end of the whiteboard);
- then as far to the left as possible (but to the right from a1), he wrote the number a3;
- then as far to the right as possible (but to the left from a2), he wrote the number a4;

Polycarp continued to act as well, until he wrote out the entire sequence on the whiteboard.
The beginning of the result looks like this (of course, if n≥4).

For example, if 𝑛=7 and 𝑎=[3,1,4,1,5,9,2], then Polycarp will write a sequence on 
the whiteboard [3,4,5,2,9,1,1].

You saw the sequence written on the whiteboard and now you want to restore Polycarp's 
favorite sequence.

Input
=====
The first line contains a single positive integer 𝑡 (1≤𝑡≤300) — the number of test cases in 
the test. Then 𝑡 test cases follow.

The first line of each test case contains an integer 𝑛 (1≤𝑛≤300) — the length of the 
sequence written on the whiteboard.

The next line contains 𝑛 integers 𝑏1,𝑏2,…,𝑏𝑛 (1≤𝑏𝑖≤109) — the sequence written on the whiteboard.

Output
Output 𝑡 answers to the test cases. Each answer — is a sequence 𝑎 that Polycarp wrote 
out on the whiteboard.
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
    n = getInt()

    array = getIntList()

    original_array = []

    left, right = 0, n-1

    if n == 1:
        print(*array)
    else:
        while left < right:
            original_array.append(array[left])
            original_array.append(array[right])
            left += 1
            right -= 1

        if n % 2 != 0:
            original_array.append(array[left])
            

        print(*original_array)

