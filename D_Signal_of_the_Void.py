




import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())



# getting the number of test cases
numOfTestCases = getInt()


for _ in range(numOfTestCases):
    # getting the data input
    numOfResidents, costToShare = getIntList()

    maxNumOfResidents = getIntList()

    costForResidentShare = getIntList()

    # getting the hubs
    hubs = sorted(zip(costForResidentShare, maxNumOfResidents))

    total_cost = costToShare
    remainder = numOfResidents - 1

    for cost, capacity in hubs:
        if remainder == 0:
            break
        
        if cost >= costToShare:
            break

        amountUse = min(capacity, remainder)

        total_cost += amountUse * cost
        remainder -= amountUse
    
    if remainder > 0:
        total_cost += remainder * costToShare
    
    print(total_cost)


