"""
There is a string 𝑎 (unknown to you), consisting of lowercase Latin letters, encrypted 
according to the following rule into string 𝑠:

1. after each character of string 𝑎, an arbitrary (possibly zero) number of any 
lowercase Latin letters, different from the character itself, is added;

2. after each such addition, the character that we supplemented is added.

You are given string 𝑠, and you need to output the initial string 𝑎. 
In other words, you need to decrypt string 𝑠


Note that each string encrypted in this way is decrypted uniquely.

Input
The first line of the input contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

The descriptions of the test cases follow. The first line of each test case 
contains a single integer 𝑛 (2≤𝑛≤100) — the length of the encrypted message.

The second line of each test case contains a string 𝑠 of length 𝑛 — the encrypted message 
obtained from some string 𝑎


Output
For each test case, output the decrypted message 𝑎 on a separate line.
"""


import sys

def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()

numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n = int(input())
    s = input().strip()

    result = []
    i = 0
    while i < len(s):
        char = s[i]
        result.append(char)
        
        # Find the next occurrence of this character
        next_pos = s.find(char, i + 1)
        if next_pos != -1:
            # Move to position after the matched character
            i = next_pos + 1
        else:
            i += 1
    
    print("".join(result))