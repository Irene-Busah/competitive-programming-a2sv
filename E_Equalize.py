"""
Vasya has two hobbies — adding permutations†
 to arrays and finding the most frequently occurring element. Recently, he found an array 𝑎
 and decided to find out the maximum number of elements equal to the same number in the array 𝑎
 that he can obtain after adding some permutation to the array 𝑎
.

More formally, Vasya must choose exactly one permutation 𝑝1,𝑝2,𝑝3,…,𝑝𝑛
 of length 𝑛
, and then change the elements of the array 𝑎
 according to the rule 𝑎𝑖:=𝑎𝑖+𝑝𝑖
. After that, Vasya counts how many times each number occurs in the array 𝑎
 and takes the maximum of these values. You need to determine the maximum value he can obtain.

†
A permutation of length 𝑛
 is an array consisting of 𝑛
 distinct integers from 1
 to 𝑛
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (𝑛=3
 but there is 4
 in the array).

Input
Each test consists of multiple test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤2⋅104
) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤2⋅105
) — the length of the array 𝑎
.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the elements of the array 𝑎
.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single number — the maximum number of elements equal to the same number after the operation of adding a permutation.


"""

import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())





