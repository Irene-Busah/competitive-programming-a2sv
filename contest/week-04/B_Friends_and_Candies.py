"""
Polycarp has n friends, the i-th of his friends has ai candies. Polycarp's friends do not like when they have different numbers of candies. 
In other words they want all ai to be the same. To solve this, Polycarp performs the following set of actions exactly once:

Polycarp chooses k (0≤k≤n) arbitrary friends (let's say he chooses friends with indices i1,i2,…,ik);
Polycarp distributes their ai1+ai2+…+aik candies among all n friends. During distribution for each of ai1+ai2+…+aik
candies he chooses new owner. That can be any of n friends. Note, that any candy can be given to the person, who has 
owned that candy before the distribution process.
Note that the number k is not fixed in advance and can be arbitrary. Your task is to find the minimum value of k


For example, if n=4 and a=[4,5,2,5], then Polycarp could make the following distribution of the candies:
    - Polycarp chooses k=2 friends with indices i=[2,4] and distributes a2+a4=10 candies to make a=[4,4,4,4] (two candies go to person 3).
Note that in this example Polycarp cannot choose k=1
 friend so that he can redistribute candies so that in the end all 𝑎𝑖
 are equal.

For the data 𝑛
 and 𝑎
, determine the minimum value 𝑘
. With this value 𝑘
, Polycarp should be able to select 𝑘
 friends and redistribute their candies so that everyone will end up with the same number of candies.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤104
). Then 𝑡
 test cases follow.

The first line of each test case contains one integer 𝑛
 (1≤𝑛≤2⋅105
).

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (0≤𝑎𝑖≤104
).

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case output:

the minimum value of 𝑘
, such that Polycarp can choose exactly 𝑘
 friends so that he can redistribute the candies in the desired way;
"-1" if no such value 𝑘
 exists.
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


# number of test cases
numOfTestCases = getInt()

for _ in range(numOfTestCases):
    numOfFriemds = getInt()

    # getting the array of friends with their candies
    candies = getIntList()

    sumOfCandies = sum(candies)

    if sumOfCandies % numOfFriemds != 0:
        print(-1)
        continue

    numOfCandiesRedistribte = sumOfCandies // numOfFriemds

    numOfSelectedFriends = 0

    for i in range(numOfFriemds):
        if candies[i] > numOfCandiesRedistribte:
            numOfSelectedFriends += 1
    
    print(numOfSelectedFriends)

    


