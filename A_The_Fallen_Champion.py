"""

"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the Youssef
battlesWon, totalTime = getIntList()

# getting the number of remaining warrior
numOfWarriors = getInt()

possible = False

for _ in range(numOfWarriors):
    numOfBattles, timeTaken = getIntList()

    if numOfBattles > battlesWon or (numOfBattles == battlesWon and timeTaken < totalTime):
        possible = True

if possible:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")


