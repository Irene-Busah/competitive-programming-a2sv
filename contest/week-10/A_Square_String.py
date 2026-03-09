"""
A string is called square if it is some string written twice in a row. For example, 
the strings "aa", "abcabc", "abab" and "baabaa" are square. But the strings "aaa", 
"abaaab" and "abcdabc" are not square.

For a given string s
 determine if it is square.

Input
The first line of input data contains an integer t (1≤t≤100) —the number of test cases.

This is followed by t lines, each containing a description of one test case. The given 
strings consist only of lowercase Latin letters and have lengths between 1 and 100 inclusive.

Output
For each test case, output on a separate line:

YES if the string in the corresponding test case is square,
NO otherwise.
You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be 
recognized as a positive response).
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


for _ in range(numOfTestCases):
    string = getStr()

    lengthOfString = len(string)

    half = lengthOfString // 2

    if lengthOfString % 2 == 0 and string[:half] == string[half:]:
        
        print("YES")
    else:
        print("NO")


    # print(string[:half], string[half:])

