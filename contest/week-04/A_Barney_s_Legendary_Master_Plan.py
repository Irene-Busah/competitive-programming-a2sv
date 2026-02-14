"""
Bro.

Barney Stinson starts with nothing. Zero. An array 𝑎
 of size 𝑛
, filled with zeros.

But Barney doesn’t do “zero.” He does legendary.

His mission is to transform this boring zero-array into a specific target lifestyle (the given array) using the minimum number of moves.

And as always, Barney has exactly two plays in his Playbook™:

Suit Up (Increase): Barney picks a positive integer 𝑥
 and adds it to every single element in the array.
Because when Barney levels up… he levels everything up.

Formally, for each 𝑖
 (1≤𝑖≤𝑛
), he replaces 𝑎𝑖
 with 𝑎𝑖+𝑥
.

Total commitment. No half-measures.


The Reset Bro (Smash): Sometimes a move isn’t working.
Barney can choose any elements (maybe none, maybe all) and reset them to 0
.

For each 𝑖
 (1≤𝑖≤𝑛
), he either keeps 𝑎𝑖
 as it is or replaces it with 0
.

Keep it. Or wipe it out completely.

New identity. New plan. New legendary opportunity.

Given the final legendary target array, determine the minimum number of total plays (Suit Up and Reset Bro) Barney needs to execute.

And trust me, Ted… no matter the target, there’s always a way to make it legendary.

It can be shown that for any given final array, a sequence of operations always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤1000
). The description of the test cases follows.

The first line contains a single integer 𝑛
 (1≤𝑛≤100
) — the number of elements in the array 𝑎
.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤100
) — the elements of the target lifestyle.

Output
For each test case, output a single integer — the minimum number of legendary plays required.
"""





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

    # for each test case, we get the length of the of the array
    lengthOfArray = getInt()

    # getting the array
    array = getIntList()

    # initial array 
    arrayCount = {}

    # print(initialArray)

    

    count = 0

    for i in range(lengthOfArray):
        # ai + x = 1 => x = 1 - ai
        if array[i] in arrayCount:
            arrayCount[array[i]] += 1
        else:
            arrayCount[array[i]] = 1
    
    minNumOfPlays = (len(arrayCount.keys()) * 2) - 1

    print(minNumOfPlays) 



