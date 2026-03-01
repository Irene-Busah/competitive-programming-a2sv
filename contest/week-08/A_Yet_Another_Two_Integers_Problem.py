"""
You are given two integers a and b.

In one move, you can choose some integer k from 1 to 10 and add it to a or subtract it from a. 
In other words, you choose an integer 𝑘∈[1;10] and perform a:=a+k or a:=a-k.
You may use different values of k in different moves.

Your task is to find the minimum number of moves required to obtain b from a.

You have to answer t independent test cases.

Input
=====
The first line of the input contains one integer t (1≤t≤2⋅104) — the number of 
test cases. Then t test cases follow.

The only line of the test case contains two integers a and b (1≤a,b≤10^9).

Output
For each test case, print the answer: the minimum number of moves required to obtain b from a

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
numOfTestCases = getInt()

for _ in range(numOfTestCases):

    a, b = getIntList()

    diff = abs(b - a)

    # print(diff)

    count = (diff + 9) // 10

    print(count)

    



