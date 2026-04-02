"""
You are given a permutation p of length n.

You must perform exactly one operation for each integer k from 1 up to n in that order:

Choose a subarray†
 of p
 of length exactly k
, and subtract 1 from every element in that subarray.
After completing all n
 operations, your goal is to have all elements of the array equal to zero.

Determine whether it is possible to achieve this.


A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (n=3
 but there is 4
 in the array).

†
An array a
 is a subarray of an array b
 if a
 can be obtained from b
 by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The first line contains the value n
 (1≤n≤100
) — the length of the permutation.

The second line contains n1,n2,…𝑝𝑛
 (1≤pi≤n
) — the permutation itself.

Output
For each test case, output YES if it is possible to make all elements of the array p
 equal to 0
 after performing all the operations; otherwise, output NO.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
"""

from utils.funcs import getInt, getIntList


numOfTestCases = getInt()


for _ in range(numOfTestCases):
    n = getInt()

    permutations = getIntList()

    # permutations.sort()

    left, right = 0, n - 1

    possible = True
    for val in range(1, n):
        if val == permutations[left]:
            left += 1
        elif val == permutations[right]:
            right -= 1
        else:
            possible = False
    
    if possible:
        print("YES")
    else:
        print("NO")

