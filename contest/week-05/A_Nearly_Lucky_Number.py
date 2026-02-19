"""
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal 
representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 
are lucky and 5, 17, 467 are not.

Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if 
the number of lucky digits in it is a lucky number. He wonders whether number n 
is a nearly lucky number.

Input
The only line contains an integer n (1≤n≤1018).

Please do not use the %lld specificator to read or write 64-bit numbers in c++. 
It is preferred to use the cin, 
cout streams or the %I64d specificator.

Output
Print on the single line "YES" if n is a nearly lucky number. 
Otherwise, print "NO" (without the quotes).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the data 
number = getStr()

arrayNum = list(number)

# counter of lucky number
count = 0

for i in range(len(arrayNum)):
    if arrayNum[i] == '4' or arrayNum[i] == '7':
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")


