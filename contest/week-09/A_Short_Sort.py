"""
There are three cards with letters a, b, c placed in a row in some order. You can do the 
following operation at most once:

Pick two cards, and swap them.
Is it possible that the row becomes abc after the operation? Output "YES" if it is possible, 
and "NO" otherwise.


Input
======
The first line contains a single integer t (1≤t≤6) — the number of test cases.

The only line of each test case contains a single string consisting of each of the three 
characters a, b, and c exactly once, representing the cards.

Output
=======
For each test case, output "YES" if you can make the row abc with at most one operation, 
or "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and 
"YES" will be recognized as a positive answer).

"""



import sys

# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the number test cases
numOfTestcases = getInt()

sorted_cards = {k:v for k, v in enumerate('abc')}

for _ in range(numOfTestcases):

    cards = getStr()

    count = 0

    
    for i in range(len(cards)):
        if cards[i] != 'abc'[i]:
            count += 1
    
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")
        

    


