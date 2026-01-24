"""
You are given an expression of the form 𝑎+𝑏, where 𝑎 and 𝑏 are integers from
 0 to 9. You have to evaluate it and print the result.

Input
The first line contains one integer 𝑡 (1≤𝑡≤100) — the number of test cases.

Each test case consists of one line containing an expression of the form 𝑎+𝑏
(0≤𝑎,𝑏≤9, both a and b are integers). The integers are not separated from 
the + sign.

Output
For each test case, print one integer — the result of the expression.
"""

import sys

def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



    

# getting the number of test cases
numOfTestCases = getInt()

# let's iterate through the expressions from 1 - numOfTestCases
for _ in range(numOfTestCases):
    expression = getStr()
    num1 = int(expression[0])
    num2 = int(expression[2])
    res = num1 + num2
    print(res)
    
 



