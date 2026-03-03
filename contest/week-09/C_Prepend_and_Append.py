"""
Timur initially had a binary string† s (possibly of length 0). He performed the following operation several (possibly zero) times:

Add 0 to one end of the string and 1 to the other end of the string. For example, starting from the string 1011, 
you can obtain either 𝟶𝟷𝟶𝟷𝟷𝟷 or 𝟷𝟷𝟶𝟷𝟷𝟶

You are given Timur's final string. What is the length of the shortest possible string he could have started with?
†
A binary string is a string (possibly the empty string) whose characters are either 0 or 1.

Input
=====
The first line of the input contains an integer t (1≤t≤100) — the number of testcases.

The first line of each test case contains an integer n (1≤n≤2000) — the length of Timur's final string.

The second line of each test case contains a string s of length n consisting of characters 0 or 1, denoting the final string.

Output
For each test case, output a single nonnegative integer — the shortest possible length of Timur's original string. 
Note that Timur's original string could have been empty, in which case you should output 0

"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# number of test cases
numOfTestcases = getInt()

for _ in range(numOfTestcases):
    lenOfStr = getInt()

    # getting the string
    string = getStr()

    left, right = 0, len(string) - 1


    while left <= right:
        if (string[left] == '1' and string[right] == '0') or (string[left] == '0' and string[right] == '1'):
            left  += 1
            right -= 1
        else:
            break
            
    print(right - left + 1)

    # while left < right and string[left] != string[right]:
    #     left  += 1
    #     right -= 1
    
    # print(right - left + 1)
