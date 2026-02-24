"""
Limak is going to participate in a contest on the last day of the 2016. The contest will start at 
20:00 and will last four hours, exactly until midnight. There will be n problems, sorted 
by difficulty, i.e. problem 1 is the easiest and problem n is the hardest. Limak knows 
it will take him 5·i minutes to solve the i-th problem.

Limak's friends organize a New Year's Eve party and Limak wants to be there at midnight 
or earlier. He needs k minutes to get there from his house, where he will participate 
in the contest first.

How many problems can Limak solve if he wants to make it to the party?

Input
The only line of the input contains two integers n and k (1≤n≤10, 1≤k≤240) — 
the number of the problems in the contest and the number of minutes Limak needs 
to get to the party from his house.

Output
Print one integer, denoting the maximum possible number of problems Limak can solve so that
he could get to the party at midnight or earlier.
"""





import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


maxNumOfHours = 60 * 4

numOfProblems, minutesToGoToParty = getIntList()

# timeForProblems = [i*5 for i in range(1, numOfProblems+1)]

sumTime = 0
counter = 0

for i in range(1, numOfProblems+1):
    sumTime += 5*i
    # print(sumTime)

    if (minutesToGoToParty + sumTime) > maxNumOfHours:
        break
    counter += 1


print(counter)

