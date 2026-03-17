"""
A class of students got bored wearing the same pair of shoes every day, so they decided to shuffle their shoes among themselves. In this problem, a pair of shoes is inseparable and is considered as a single object.

There are 𝑛
 students in the class, and you are given an array 𝑠
 in non-decreasing order, where 𝑠𝑖
 is the shoe size of the 𝑖
-th student. A shuffling of shoes is valid only if no student gets their own shoes and if every student gets shoes of size greater than or equal to their size.

You have to output a permutation 𝑝
 of {1,2,…,𝑛}
 denoting a valid shuffling of shoes, where the 𝑖
-th student gets the shoes of the 𝑝𝑖
-th student (𝑝𝑖≠𝑖
). And output −1
 if a valid shuffling does not exist.

A permutation is an array consisting of 𝑛
 distinct integers from 1
 to 𝑛
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array) and [1,3,4]
 is also not a permutation (𝑛=3
 but there is 4
 in the array).

Input
Each test contains multiple test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤1000
) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤105
) — the number of students.

The second line of each test case contains 𝑛
 integers 𝑠1,𝑠2,…,𝑠𝑛
 (1≤𝑠𝑖≤109
, and for all 1≤𝑖<𝑛
, 𝑠𝑖≤𝑠𝑖+1
) — the shoe sizes of the students.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105
.

Output
For each test case, print the answer in a single line using the following format.

If a valid shuffling does not exist, print the number −1
 as the answer.

If a valid shuffling exists, print 𝑛
 space-separated integers — a permutation 𝑝
 of 1,2,…,𝑛
 denoting a valid shuffling of shoes where the 𝑖
-th student gets the shoes of the 𝑝𝑖
-th student. If there are multiple answers, then print any of them.


"""

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
    numOfStudents = getInt()

    shoeSizes = getIntList()

    permutations = [0] * numOfStudents


    i = 0
    possible = True

    while i < numOfStudents:
        j = i

        while j < numOfStudents and shoeSizes[i] == shoeSizes[j]:
            j += 1
        
        if j - i == 1:
            possible = False
            break

        # arranging the shoes
        for k in range(i, j-1):
            permutations[k] = k + 2
        permutations[j-1] = i + 1

        i = j
    if possible:
        print(*permutations)
    else:
        print(-1)
    # print(*permutations if possible else -1)




