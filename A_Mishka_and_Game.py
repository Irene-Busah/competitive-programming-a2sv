"""
Mishka is a little polar bear. As known, little bears loves spending their free time playing dice 
for chocolates. Once in a wonderful sunny morning, walking around blocks of ice, Mishka met her 
friend Chris, and they started playing the game.

Rules of the game are very simple: at first number of rounds n is defined. In every round each 
of the players throws a cubical dice with distinct numbers from 1 to 6 written on its faces. 
Player, whose value after throwing the dice is greater, wins the round. In case if player 
dice values are equal, no one of them is a winner.

In average, player, who won most of the rounds, is the winner of the game. In case if two 
players won the same number of rounds, the result of the game is draw.

Mishka is still very little and can't count wins and losses, so she asked you to watch their 
game and determine its result. Please help her!

Input
=====
The first line of the input contains single integer n n (1≤n≤100) — the number of game rounds.

The next n lines contains rounds description. i-th of them contains pair of integers mi and 
ci (1≤mi,ci≤6) — values on dice upper face after Mishka's and Chris' throws in i-th 
round respectively.

Output
If Mishka is the winner of the game, print "Mishka" (without quotes) in the only line.

If Chris is the winner of the game, print "Chris" (without quotes) in the only line.

If the result of the game is draw, print "Friendship is magic!^^" (without quotes) in the only line.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfGameRounds = getInt()

mishkaWins = 0
chrisWins = 0

for i in range(numOfGameRounds):
    m, c = getIntList()

    if m > c:
        mishkaWins += 1
    elif c > m:
        chrisWins += 1
    else:
        mishkaWins += 0
        chrisWins += 0
    
if mishkaWins > chrisWins:
    print("Mishka")
elif chrisWins > mishkaWins:
    print("Chris")
else:
    print("Friendship is magic!^^")

