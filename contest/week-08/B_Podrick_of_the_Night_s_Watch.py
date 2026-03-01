"""

"""


from collections import defaultdict
from math import ceil
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfDays = getInt()

counter = {}

need = ceil(0.8 * numOfDays)

for _ in range(numOfDays):
    numOfMessages = getInt()

    for _ in range(numOfMessages):
        ravenName, hour = getStrList()

        key = (ravenName, int(hour))

        counter[key] = counter.get(key, 0) + 1

        if counter[key] >= need:
            print("YES")
            sys.exit(0)

print("NO")

