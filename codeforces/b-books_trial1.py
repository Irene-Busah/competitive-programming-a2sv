import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting input data
numOfBooks, freeMinutes = getIntList()

books = getIntList()

completedBooks = 0

minutesSpent = 0

left = 0

for right in range(numOfBooks):
    minutesSpent += books[right]

    while minutesSpent > freeMinutes:
        minutesSpent -= books[left]

        left += 1
    
    completedBooks = max(completedBooks, right - left + 1)


print(completedBooks)