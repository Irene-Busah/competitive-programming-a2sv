"""
The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: 
a Berlandish word differs from a Birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. 
For example, a Berlandish word, code, corresponds to a Birlandish word, edoc. However, making a mistake during the "translation" 
is easy. Vasya translated the word s from Berlandish into Birlandish as, t. Help him: find out if he translated the word correctly.

Input
=====
The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters. 
The input data do not contain unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

Output
======
If the word t is a word s, written reversely, print YES, otherwise print NO.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# Berland word
berland_word = getStr()

# Borland word
birland_word = getStr()

reversed_berland_word = berland_word[::-1]

if reversed_berland_word == birland_word:
    print('YES')
else:
    print('NO')


# print(reversed_berland_word, birland_word)



