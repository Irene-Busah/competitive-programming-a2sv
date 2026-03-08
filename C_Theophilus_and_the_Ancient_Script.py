"""
Theophilus, a master of ancient sequence alignment, has been tasked with reorganizing a series of 𝐴
 and 𝐵
 symbols found on a crumbling scroll. Each symbol holds a specific energy, and by swapping an 𝐴
 with a 𝐵
, he can release a fragment of forgotten knowledge. However, the scroll's structure is delicate; the boundary between any two adjacent symbols can only withstand the friction of a single swap. Theophilus must strategically choose the order of his movements to extract as much knowledge as possible.

You are given a string 𝑠
 of length 𝑛
 consisting of characters 𝙰
 and 𝙱
. You are allowed to do the following operation:

Choose an index 1≤𝑖≤𝑛−1
 such that 𝑠𝑖=𝙰
 and 𝑠𝑖+1=𝙱
. Then, swap 𝑠𝑖
 and 𝑠𝑖+1
.
You are only allowed to do the operation at most once for each index 1≤𝑖≤𝑛−1
. However, you can do it in any order you want. Find the maximum number of operations that you can carry out.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤1000
). Description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (2≤𝑛≤2⋅105
) — the length of string 𝑠
.

The second line of each test case contains the string 𝑠
 (𝑠𝑖=𝙰
 or 𝑠𝑖=𝙱
).

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print a single integer containing the maximum number of operations that you can carry out.
"""



# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting input data
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    lengthOfString = getInt()

    string = getStr()

    left = 0
    right = lengthOfString - 1

    while left < lengthOfString and string[left] != 'A':
        left += 1
    
    while right >= 0 and string[right] != 'B':
        right -= 1
    
    if left < right:
        print(right-left)
    else:
        print(0)


