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


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(arr1)):
            if arr1[i] not in hashmap:
                hashmap[arr1[i]] = 1
            else:
                hashmap[arr1[i]] += 1
        
        for i in arr2:
            while hashmap[i] > 0:
                res.append(i)
                hashmap[i] -= 1
        
        for key in sorted(hashmap.keys()):
            while hashmap[key] > 0:
                res.append(key)

                hashmap[key] -= 1

        print(res)


if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    Solution().relativeSortArray(arr1, arr2)

