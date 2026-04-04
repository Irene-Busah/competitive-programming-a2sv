"""
You were walking down the street and heard a sound. The sound was described by the string s
consisting of lowercase and uppercase Latin characters. Now you want to find out if the sound was a cat meowing.

For the sound to be a meowing, the string can only contain the letters 'm', 'e', 'o' and 'w', in either uppercase or lowercase. Also:

string must start with non-empty sequence consisting only of characters 'm' or 'M'
it must be immediately followed by non-empty sequence consisting only of characters 'e' or 'E'
it must be immediately followed by non-empty sequence consisting only of characters 'o' or 'O'
it must be immediately followed by non-empty sequence consisting only of characters 'w' or 'W', this sequence ends the string, 
after it immediately comes the string end
For example, strings "meow", "mmmEeOWww", "MeOooOw" describe a meowing, but strings "Mweo", "MeO", "moew", "MmEW", "meowmeow" do not.

Determine whether the sound you heard was a cat meowing or something else.

Input
The first line of input data contains a single integer t (1≤t≤104) — the number of test cases.

The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤50) — the length of the string describing the sound.

The second line of each test case contains a string s of n
characters. The string describes the sound you heard and consists only of lowercase and uppercase Latin letters.

Output
For each test case, output on a separate line:

YES if the sound was a cat meowing;
NO otherwise.
You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as positive response).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestCases = getInt()

sound = 'MEOW'

for _ in range(numOfTestCases):
    n = getInt()

    string = getStr().lower()

    newString = string[0]

    for i in range(1, n):
        if string[i] != string[i-1]:
            newString += string[i]
    
    if newString.upper() == sound:
        print("YES")
    else:
        print("NO")





