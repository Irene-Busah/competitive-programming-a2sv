"""
Xenia the beginner mathematician is a third year student at elementary school. 
She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. 
To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't 
enough for Xenia. She is only beginning to count, so she can 
calculate a sum only if the summands follow in non-decreasing order. For example, she can't 
calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum 
in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. 
It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. 
String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


math_str = getStr().split('+')

math_str = sorted(math_str)


print('+'.join(math_str))




