"""
We all know that a superhero can transform to certain other superheroes. But not all Superheroes can transform to any other superhero. A superhero with name 𝑠
 can transform to another superhero with name 𝑡
 if 𝑠
 can be made equal to 𝑡
 by changing any vowel in 𝑠
 to any other vowel and any consonant in 𝑠
 to any other consonant. Multiple changes can be made.

In this problem, we consider the letters 'a', 'e', 'i', 'o' and 'u' to be vowels and all the other letters to be consonants.

Given the names of two superheroes, determine if the superhero with name 𝑠
 can be transformed to the Superhero with name 𝑡
.

Input
The first line contains the string 𝑠
 having length between 1
 and 1000
, inclusive.

The second line contains the string 𝑡
 having length between 1
 and 1000
, inclusive.

Both strings 𝑠
 and 𝑡
 are guaranteed to be different and consist of lowercase English letters only.

Output
Output "Yes" (without quotes) if the superhero with name 𝑠
 can be transformed to the superhero with name 𝑡
 and "No" (without quotes) otherwise.

You can print each letter in any case (upper or lower).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


s = getStr()
t = getStr()

vowels = ['a', 'e', 'i', 'o', 'u']

def is_vowel(char):
    return char in vowels    
if len(s) != len(t):
    print("No")
else:
    possible = True
    for i in range(len(s)):
            if is_vowel(s[i]) != is_vowel(t[i]):
                possible = False
                break

    if possible:
        print("Yes")
    else:
        print('No')

# consonants = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z]

