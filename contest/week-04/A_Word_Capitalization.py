"""
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize 
the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. 
The length of the word will not exceed 103.

Output
Output the given word after capitalization.
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
word = list(getStr())

if word[0].lower():
    word[0] = word[0].upper()

print(''.join(word))



