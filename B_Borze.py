"""
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number 
the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». 
You are to decode the Borze code, i.e. to find out the ternary number given its 
representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is 
between 1 and 200 characters. It's guaranteed that the given string is a valid 
Borze code of some ternary number (this number can have leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.
"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()


code = {'.': '0', '-.': '1', '--':'2'}

borzoCode = getStr()

res = []

i = 0

while i < len(borzoCode):
    if borzoCode[i] == '.':
        res.append(code['.'])
        i += 1
    else:
        pair = borzoCode[i:i+2]
        res.append(code[pair])

        i += 2


print("".join(res))
