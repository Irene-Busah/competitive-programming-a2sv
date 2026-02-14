"""
You are given a sequence of 𝑛
 mechanical timers arranged in a straight line. The initial value displayed on the 𝑖
-th timer is 𝑎𝑖
.

Every second, the following events occur in order:

The value on each timer decreases by 1
. If the value of any timer becomes 0
, you immediately lose.
You may move to an adjacent timer (to the left or right) or remain at your current timer.
You may reset the timer you are currently standing on back to its original value 𝑎𝑖
.
Note that these events happen strictly in the given order. If the value of a timer becomes 0
 during the first step of a second, you lose instantly, even if you could move to that timer and reset it later during the same second.

You may start at any timer. Determine whether it is possible to continue this process indefinitely without losing.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

For each test case, the first line contains a single integer 𝑛
 (2≤𝑛≤5⋅105
) — the number of timers.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the initial values of the timers.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 5⋅105
.

Output
For each test case, print "YES" (without quotes) if it is possible to continue the process indefinitely, or "NO" (without quotes) otherwise.

You may print "YES" and "NO" in any letter case (for example, "yEs", "yes", and "Yes" will all be accepted as correct).
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the number of test cases
numOfTestCases = getInt()


for _ in range(numOfTestCases):
    numOfTimers = getInt()

    timers = getIntList()

    possible = True

    for i in range(numOfTimers):
        maxMoves = 2 * max(i, numOfTimers-1-i)

        if timers[i] <= maxMoves:
            possible = False
            break
    
    print("YES" if possible else "NO")



