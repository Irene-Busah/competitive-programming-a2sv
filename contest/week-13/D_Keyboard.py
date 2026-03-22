from re import S
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
    string = getStr()

    i = 0
    workingKeys = set()

    while i < len(string):
        j = i

        while j < len(string) and string[i] == string[j]:
            j += 1
        
        length = j - i

        if length % 2 == 1:
            workingKeys.add(string[i])
        i = j
    print(''.join(sorted(workingKeys)))


