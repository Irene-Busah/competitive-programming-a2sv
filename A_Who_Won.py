"""
Kevin loves watching football. In such a game, the score on the scoreboard is represented as x : y, where x is the number of goals of the first team, and y is the number of goals of the second team. At any given time, only one team can score a goal, so the score x : y can change to either (x+1) : y, or x : (y+1).

While watching a Premier League football game Arsenal Vs Manchester United, Kevin was contacted by Kidus to maintain his consistency and went to solve problem, and after some time, he returned to watching the game. Kevin remembers the score right before he was contacted, and the score right after he returned. Given these two scores, he wonders the following question. Is it possible that, while Kevin was not watching the game, the teams never had an equal score?

It is guaranteed that at neither of the two time points Kevin remembers the teams had equal scores. However, it is possible that the score did not change during his absence.

Help Kevin and answer the question!

Input
Each test consists of several test cases. The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers 𝑥1,𝑦1
 (0≤𝑥1,𝑦1≤109
, 𝑥1≠𝑦1
) — the score before Kevin was contacted by Kidus.

The second line of each test case contains two integers 𝑥2,𝑦2
 (𝑥1≤𝑥2≤109
, 𝑦1≤𝑦2≤109
, 𝑥2≠𝑦2
) — the score when Kevin returned.

Output
For each test case, output "YES" without quotes if it is possible, that the teams never had a tie while Kevin was away, otherwise output "NO" without quotes.

You can output each letter in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).
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
    x1, y1 = getIntList()
    x2, y2 = getIntList()

    if (x1 - y1) * (x2 - y2) > 0:
        print("YES")
    else:
        print("NO")

