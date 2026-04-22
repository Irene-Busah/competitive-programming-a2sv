"""
Mark is cleaning a row of 𝑛
 rooms. The 𝑖
-th room has a nonnegative dust level 𝑎𝑖
. He has a magical cleaning machine that can do the following three-step operation.

Select two indices 𝑖<𝑗
 such that the dust levels 𝑎𝑖
, 𝑎𝑖+1
, …
, 𝑎𝑗−1
 are all strictly greater than 0
.
Set 𝑎𝑖
 to 𝑎𝑖−1
.
Set 𝑎𝑗
 to 𝑎𝑗+1
.
Mark's goal is to make 𝑎1=𝑎2=…=𝑎𝑛−1=0
 so that he can nicely sweep the 𝑛
-th room. Determine the minimum number of operations needed to reach his goal.
Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains a single integer 𝑛
 (2≤𝑛≤2⋅105
) — the number of rooms.

The second line of each test case contains 𝑛
 integers 𝑎1
, 𝑎2
, ..., 𝑎𝑛
 (0≤𝑎𝑖≤109
) — the dust level of each room.

It is guaranteed that the sum of 𝑛
 across all test cases does not exceed 2⋅105
.

Output
For each test case, print a line containing a single integer — the minimum number of operations. 
It can be proven that there is a sequence of operations that meets the goal.
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
    n = getInt()

    dustLevel = getIntList()

    relevant = dustLevel[:n-1]
    
    # Check if all rooms are already clean
    has_dust = False
    for dust in relevant:
        if dust > 0:
            has_dust = True
            break
    
    if not has_dust:
        print(0)
        continue
    
    # Count the sum of dust
    total_sum = sum(relevant)
    
    # Count the number of contiguous segments with positive dust
    segments = 0
    in_segment = False
    for dust in relevant:
        if dust > 0:
            if not in_segment:
                segments += 1
                in_segment = True
        else:
            in_segment = False
    
    # Answer = sum of dust + max(segments-1, 1)
    result = total_sum + max(segments - 1, 1)
    
    print(result)

