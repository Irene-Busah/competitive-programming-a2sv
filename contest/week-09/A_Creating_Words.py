"""
Matthew is given two strings a and b, both of length 3. He thinks it's particularly 
funny to create two new words by swapping the first character of a with the first character of b

He wants you to output a and b after the swap.

Note that the new words may not necessarily be different.

Input
The first line contains t (1≤t≤100)  — the number of test cases.

The first and only line of each test case contains two space-separated strings, a and b, 
both of length 3. The strings only contain lowercase Latin letters.

Output
For each test case, after the swap, output a and b, separated by a space.
"""


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

for _ in range(numOfTestCases):
    firstWord, secondWord = getStrList()

    # ====== First Approach (O(1) - time complexity & O(n) - space complexity)
    firstWord = list(firstWord)
    secondWord = list(secondWord)


    tmp = firstWord[0]
    firstWord[0] = secondWord[0]
    secondWord[0] = tmp

    print("".join(firstWord), "".join(secondWord))



