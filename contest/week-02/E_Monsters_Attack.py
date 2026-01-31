"""
You are playing a computer game. The current level of this game can be modeled as a straight line. Your character is in point 0
 of this line. There are 𝑛
 monsters trying to kill your character; the 𝑖
-th monster has health equal to 𝑎𝑖
 and is initially in the point 𝑥𝑖
.

Every second, the following happens:

first, you fire up to 𝑘
 bullets at monsters. Each bullet targets exactly one monster and decreases its health by 1
. For each bullet, you choose its target arbitrary (for example, you can fire all bullets at one monster, fire all bullets at different monsters, or choose any other combination). Any monster can be targeted by a bullet, regardless of its position and any other factors;
then, all alive monsters with health 0
 or less die;
then, all alive monsters move 1
 point closer to you (monsters to the left of you increase their coordinates by 1
, monsters to the right of you decrease their coordinates by 1
). If any monster reaches your character (moves to the point 0
), you lose.
Can you survive and kill all 𝑛
 monsters without letting any of them reach your character?

Input
The first line of the input contains one integer 𝑡
 (1≤𝑡≤3⋅104
) — the number of test cases.

Each test case consists of three lines:

the first line contains two integers 𝑛
 and 𝑘
 (1≤𝑛≤3⋅105
; 1≤𝑘≤2⋅109
);
the second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
);
the third line contains 𝑛
 integers 𝑥1,𝑥2,…,𝑥𝑛
 (−𝑛≤𝑥1<𝑥2<𝑥3<⋯<𝑥𝑛≤𝑛
; 𝑥𝑖≠0
).
Additional constraint on the input: the sum of 𝑛
 over all test cases does not exceed 3⋅105
.

Output
For each test case, print YES if you can kill all 𝑛
 monsters before they reach your character, or NO otherwise.

You can output each letter of the answer in any case (upper or lower). For example, the strings yEs, yes, Yes, and YES will all be recognized as positive responses.
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


# getting all the input data
numOfTestCases = getInt()

for i in range(numOfTestCases):
    numOfMonsters, numOfBullets = getIntSeq()
    monstersHealth = getIntList()
    monstersPosition = getIntList()

    healthByDistance = [0] * (numOfMonsters + 1)

    for ai, xi in zip(monstersHealth, monstersPosition):
        distance = abs(xi)
        healthByDistance[distance] += ai
    
    total = 0
    status = True

    for dist in range(1, numOfMonsters+1):
        total += healthByDistance[dist]
        if total > numOfBullets * dist:
            status = False
            break
    
    print("YES" if status else "NO")

