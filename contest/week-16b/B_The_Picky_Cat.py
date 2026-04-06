"""
You are given an array of integers 𝑎1,𝑎2,…,𝑎𝑛
. You are allowed to do the following operation any number of times (possibly zero):

Choose an index 𝑖
 (1≤𝑖≤𝑛
). Multiply 𝑎𝑖
 by −1
 (i.e., update 𝑎𝑖:=−𝑎𝑖
).
Your task is to determine whether it is possible to make the element at index 1
 become the median of the array after doing the above operation any number of times. Note that operations can be applied to index 1
 as well, meaning the median can be either the original value of 𝑎1
 or its negation.

The median of an array 𝑏1,𝑏2,…,𝑏𝑚
 is defined as the ⌈𝑚2⌉
-th∗
 smallest element of array 𝑏
. For example, the median of the array [3,1,2]
 is 2
, while the median of the array [10,1,8,3]
 is 3
.

It is guaranteed that the absolute value of the elements of 𝑎
 are distinct. Formally, there are no pairs of indices 1≤𝑖<𝑗≤𝑛
 where |𝑎𝑖|=|𝑎𝑗|
.

∗
⌈𝑥⌉
 is the ceiling function which returns the least integer greater than or equal to 𝑥
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤105
) — the length of the array 𝑎
.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (|𝑎𝑖|≤106
, |𝑎𝑖|≠|𝑎𝑗|
) — the elements of the array 𝑎
.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105
.

Output
For each testcase, output "YES" if it is possible to make the element at index 1
 become the median of the array, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
"""


from math import ceil
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
    n = getInt()

    arrayA = getIntList()

    sortedArray = sorted(arrayA)

    k = (n+1)// 2

    x = abs(arrayA[0])

    count = 0 # number of elements less than x

    for i in range(1, n):
        if abs(arrayA[i]) < x:
            count += 1
    
    if count <= n - k:
        print("YES")
    else:
        print("NO")

    # print(expectedmedian)


