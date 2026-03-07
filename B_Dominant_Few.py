"""
You are given a sequence of 𝑛
 non-negative integers 𝑎1,𝑎2,…,𝑎𝑛
. Each number represents the skill level of a player.

Initially, no player belongs to any team. You may assign each player to Team Elite, Team Crowd, or leave them unassigned.

For a team 𝑡
, Count(𝑡)
 is the number of players assigned to that team and Skill(𝑡)
 is the sum of the skill levels of players assigned to that team.

For example, if the given sequence is [2,8,6,3,1]
 and player 6
 is assigned to Team Elite while players 2
 and 3
 are assigned to Team Crowd (and the other players remain unassigned), then Skill(Elite)=6
, Skill(Crowd)=2+3=5
, Count(Elite)=1
, and Count(Crowd)=2
.

Determine if it is possible to assign players such that Skill(Elite)>Skill(Crowd)
 and Count(Elite)<Count(Crowd)
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤1000
). Description of the test cases follows.

The first line of each test case contains an integer 𝑛
 (3≤𝑛≤2⋅105
) — the number of players.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖≤109
) — the skill levels.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print YES if it is possible to assign the players satisfying the conditions, and NO otherwise.

You can output YES and NO in any case (for example, yEs, yes, Yes, and YES will be recognized as positive responses).
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


# getting the input data
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    numOfPlayers = getInt()

    players = getIntList()

    players.sort()

    left, right = 1, numOfPlayers - 1

    elite = players[-1]
    crowd = players[0] + players[1]

    while left + 1 < right and elite <= crowd:
        left += 1
        right -= 1

        elite += players[right]
        crowd += players[left]
    

    print("YES" if crowd < elite else "NO")


        # if cardNums[left] > cardNums[right]:
        #     chosen_card = cardNums[left]
        #     left += 1
        # else:
        #     chosen_card = cardNums[right]
        #     right -= 1

        # if turns == 0:
        #     S_score += chosen_card
        # else:
        #     D_score += chosen_card


