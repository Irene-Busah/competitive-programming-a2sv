"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. 
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:
==========
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.


Example 2:
===========
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.


Example 3:
==========
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

"""

from itertools import count
import re
from typing import Counter, List


# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:

#         # =========== First Approach - bubble sort =========
#         # getting array size
#         arraySize = len(nums)

#         res = []

#         # for i in range(arraySize):
#         #     for j in range(arraySize-i-1):
#         #         if nums[j] > nums[j+1]:
#         #             nums[j], nums[j+1] = nums[j+1], nums[j]

#         # for i in range(arraySize):
#         #     if nums[i] == target:
#         #         res.append(i)
        
#         # print(res)



#         # ============== Second approach ==============

#         nums.sort()


#         for i in range(arraySize):
#             if nums[i] == target:
#                 res.append(i)
        
#         print(res) 



"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         hashmap = {}
#         res = []

#         for i in range(len(arr1)):
#             if arr1[i] not in hashmap:
#                 hashmap[arr1[i]] = 1
#             else:
#                 hashmap[arr1[i]] += 1
        
#         for i in arr2:
#             while hashmap[i] > 0:
#                 res.append(i)
#                 hashmap[i] -= 1
        
#         for key in sorted(hashmap.keys()):
#             while hashmap[key] > 0:
#                 res.append(key)

#                 hashmap[key] -= 1

#         print(res)




"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.

 

Example 1:
==========
Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.


Example 2:
==========
Input: piles = [2,4,5]
Output: 4
Example 3:

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18
"""


# class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
#         soted_array = sorted(piles)

#         if len(piles) % 3 != 0:
#             return





"""
Given an integer array nums, your goal is to make all elements in nums equal. 
To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. 
If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
 

Example 1:
===========
Input: nums = [5,1,3]
Output: 3
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].


Example 2:
==========
Input: nums = [1,1,1]
Output: 0
Explanation: All elements in nums are already equal.
Example 3:

Input: nums = [1,1,2,2,3]
Output: 4
"""



# class Solution:
#     def reductionOperations(self, nums: List[int]) -> int:
#         # initialize counter
#         count = 0

#         nums.sort()

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 count += len(nums) - i

#         print(count)




"""
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:
===========
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
==========
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
==========
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}

        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1
        
        res = [v*k for k, v in sorted(counter.items(), key=lambda x: -x[1])]

        print("".join(res), counter)




if __name__ == '__main__':
    s = "tree"

    # s = "cccaaa"

    # s = "Aabb"

    Solution().frequencySort(s)

