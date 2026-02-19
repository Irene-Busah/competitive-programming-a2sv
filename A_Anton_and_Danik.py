"""
Anton likes to play chess, and so does his friend Danik.

Once they have played n games in a row. For each game it's known who was the winner — 
Anton or Danik. None of the games ended with a tie.

Now Anton wonders, who won more games, he or Danik? Help him determine this.

Input
The first line of the input contains a single integer n (1≤n≤100000) — 
the number of games played.

The second line contains a string s, consisting of n uppercase English letters 'A' and 'D' 
— the outcome of each of the games. The i-th character of the string is equal to 'A' if 
the Anton won the i-th game and 'D' if Danik won the i-th game.

Output
If Anton won more games than Danik, print "Anton" (without quotes) in the only line of the output.

If Danik won more games than Anton, print "Danik" (without quotes) in the only line of the output.

If Anton and Danik won the same number of games, print "Friendship" (without quotes).
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of games
numOfGames = getInt()

# getting the games winners
games = getStr()

anton_count = 0
danik_count = 0

for i in range(numOfGames):
    if games[i] == 'A':
        anton_count += 1
    else:
        danik_count += 1

if anton_count > danik_count:
    print('Anton')
elif anton_count < danik_count:
    print('Danik')
else:
    print('Friendship')

# print(games)


