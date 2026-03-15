"""
The High Council of Canine Aesthetics has long prided itself on the absolute visual harmony of the realm's pets, where every litter is expected to be a perfect, singular hue. This morning, however, a shocking report from the breeding grounds has sent the Council into an uproar, as the latest generation has defied all standards of uniformity.

Panic is rising in the committee for doggo standardization — the puppies of the new brood have been born multi-colored! In total there are 26 possible colors of puppies in the nature and they are denoted by letters from 'a' to 'z' inclusive.

The committee rules strictly prohibit even the smallest diversity between doggos and hence all the puppies should be of the same color. Thus Slava, the committee employee, has been assigned the task to recolor some puppies into other colors in order to eliminate the difference and make all the puppies have one common color.

Unfortunately, due to bureaucratic reasons and restricted budget, there's only one operation Slava can perform: he can choose a color 𝑥
 such that there are currently at least two puppies of color 𝑥
 and recolor all puppies of the color 𝑥
 into some arbitrary color 𝑦
. Luckily, this operation can be applied multiple times (including zero).

For example, if the number of puppies is 7
 and their colors are represented as the string "abababc", then in one operation Slava can get the results "zbzbzbc", "bbbbbbc", "aaaaaac", "acacacc" and others. However, if the current color sequence is "abababc", then he can't choose 𝑥
='c' right now, because currently only one puppy has the color 'c'.

Help Slava and the committee determine whether it is possible to standardize all the puppies, i.e. after Slava's operations all the puppies should have the same color.

Input
The first line contains a single integer 𝑛
 (1≤𝑛≤105
) — the number of puppies.

The second line contains a string 𝑠
 of length 𝑛
 consisting of lowercase Latin letters, where the 𝑖
-th symbol denotes the 𝑖
-th puppy's color.

Output
If it's possible to recolor all puppies into one color, print "Yes".

Otherwise print "No".

Output the answer without quotation signs.
"""



import sys

from typing import Counter


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



numOfPuppies = getInt()

puppiesColors = list(getStr())

counter = Counter(puppiesColors)

if numOfPuppies == 1 or any(val >= 2 for val in counter.values()):
    print("Yes")
# elif :
#     print("Yes")
else:
    print("No")


# print(puppiesColors)

