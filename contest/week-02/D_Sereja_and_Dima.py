"""
Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row. Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first. During his turn a player can take one card: either the leftmost card in a row, or the rightmost one. The game ends when there is no more cards. The player who has the maximum sum of numbers on his cards by the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Inna is a friend of Sereja and Dima. She knows which strategy the guys are using, so she wants to determine the final score, given the initial state of the game. Help her.

Input
The first line contains integer n — the number of cards on the table. The second line contains space-separated numbers on the cards from left to right. The numbers on the cards are distinct integers from 1 to 1000.

Output
On a single line, print two integers. The first number is the number of Sereja's points at the end of the game, the second number is the number of Dima's points at the end of the game.
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


# getting the number of cards
numOfCards = getInt()

# getting the card numbers
cardNums = getIntList()

S_score = 0
D_score = 0

# Sereja starts first - 0 & Dimja follows - 1
turns = 0

# 1 2 3 4 5 6 7
# s=7+5+3+1 d=6+4+2

left = 0
right = numOfCards - 1

while left <= right:
    if cardNums[left] > cardNums[right]:
        chosen_card = cardNums[left]
        left += 1
    else:
        chosen_card = cardNums[right]
        right -= 1

    if turns == 0:
        S_score += chosen_card
    else:
        D_score += chosen_card
    
    turns = 1 - turns

print(S_score, D_score)