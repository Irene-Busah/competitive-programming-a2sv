"""
Upon arriving at school, Macaque was rather brusquely greeted by his friend, AG-88301, the latter having skived off his homework due to spending the entire night yapping to an unsuspecting stranger about his groundbreaking work on a proof of the Collatz conjecture and his 67
-th unreciprocated love interest. So, as had become customary, AG-88301, with ever decreasing levels of gratitude or appreciation, made Macaque do his homework for him. At this point, Macaque had had enough, and turned to his minions (you guys!) to solve AG-88301's homework task.

You are given an integer 𝑛
. You must construct a permutation∗
 of length 3𝑛
 such that, if you partition the permutation into 𝑛
 contiguous blocks with 3
 elements, the sum of the medians†
 of these blocks is maximised.

More formally, you must construct a permutation 𝑝
 of length 3𝑛
 such that ∑𝑛−1𝑖=0median(𝑎3𝑖+1,𝑎3𝑖+2,𝑎3𝑖+3)
 is maximised. If there are multiple possible 𝑝
, output any.

∗
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

†
The median of an array 𝑏
 containing 3
 elements is the 2
-nd element after 𝑏
 is sorted in non-decreasing order.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first and only line of each test case contains an integer 𝑛
 (1≤𝑛≤105
).

It is guaranteed that the sum of 3𝑛
 does not exceed 3⋅105
 over all test cases.

Output
For each test case, output a permutation 𝑝
 such that the sum of the medians of the contiguous blocks is maximised. If there are multiple possible 𝑝
, output any.
"""


from utils.funcs import getInt


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n = getInt()

    array = []
    left = 1
    right = 3*n
    for _ in range(n):
        array.append(left)       
        array.append(right-1)    
        array.append(right)      
        left += 1
        right -= 2

    print(*array)



