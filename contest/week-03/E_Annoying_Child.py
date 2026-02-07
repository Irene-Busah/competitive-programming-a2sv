

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# getting the number of test cases, t
numOfTestCases = getInt()


for _ in range(numOfTestCases):
    numOfCoins = getInt()
    coins = getIntList()

    evens = sorted([x for x in coins if x % 2 == 0], reverse=True)
    odds  = sorted([x for x in coins if x % 2 == 1], reverse=True)

    if len(odds) == 0:
        print(*([0] * numOfCoins))
        continue

    bestOdd = odds[0]
    E = len(evens)
    O = len(odds)

    # prefix sums of evens: pref[i] = sum of top i evens
    pref = [0] * (E + 1)
    for i in range(E):
        pref[i + 1] = pref[i] + evens[i]

    answers = []

    for k in range(1, numOfCoins + 1):
        if k - 1 <= E:
            answers.append(bestOdd + pref[k - 1])
        else:
            need = (k - 1) - E

            if need % 2 == 0 and need <= (O - 1):
                answers.append(bestOdd + pref[E])
            elif E >= 1 and (need + 1) <= (O - 1):
                answers.append(bestOdd + pref[E - 1])
            else:
                answers.append(0)

    print(*answers)



