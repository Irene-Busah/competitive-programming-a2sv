"""
Each day in Berland consists of 𝑛
 hours. Polycarp likes time management. That's why he has a fixed schedule for each day — it is a sequence 𝑎1,𝑎2,…,𝑎𝑛
 (each 𝑎𝑖
 is either 0
 or 1
), where 𝑎𝑖=0
 if Polycarp works during the 𝑖
-th hour of the day and 𝑎𝑖=1
 if Polycarp rests during the 𝑖
-th hour of the day.

Days go one after another endlessly and Polycarp uses the same schedule for each day.

What is the maximal number of continuous hours during which Polycarp rests? It is guaranteed that there is at least one working hour in a day.

Input
The first line contains 𝑛
 (1≤𝑛≤2⋅105
) — number of hours per day.

The second line contains 𝑛
 integer numbers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖≤1
), where 𝑎𝑖=0
 if the 𝑖
-th hour in a day is working and 𝑎𝑖=1
 if the 𝑖
-th hour is resting. It is guaranteed that 𝑎𝑖=0
 for at least one 𝑖
.

Output
Print the maximal number of continuous hours during which Polycarp rests. Remember that you should consider that days go one after another endlessly and Polycarp uses the same schedule for each day.
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfHours = getInt()



array = getIntList()

new_array = array + array

count = 0
current = 0

for val in new_array:
    if val == 1:
        current += 1
        count = max(count, current)
    else:
        current = 0

    # if array[-1] == 
    
print(min(count, numOfHours)) 



