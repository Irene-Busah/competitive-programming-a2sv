"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""


# libraries
from typing import List




# class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     maxSum = float('-inf')
    #     currSum = 0

    #     left = 0

    #     for right in range(len(nums)):
    #         currSum += nums[right]

    #         if right - left + 1 > k:
    #             currSum -= nums[left]
    #             left += 1
            
    #         maxSum = max(currSum, maxSum)
            
    #     return maxSum / k



"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         res = 0
#         window = set()

#         left = 0

#         for right in range(len(s)):     

#             while s[right] in window:
#                 window.remove(s[left])
                
#                 left += 1
#             window.add(s[right])
#             res = max(res, right - left + 1)

#         return res



"""
Given an array of n integers ai. Let's say that the segment of this array a[l..r] (1≤l≤r≤n) is good if the sum of elements
on this segment is at most S. Your task is to find the longest good segment.

Input
=====
The first line contains integers n and s (1≤n≤105, 1≤s≤1018). The second line contains integers ai (1<=aii≤109).

Output
======
Print one integer, the length of the longest good segment. If there are no such segments, print 0.
"""


# import sys


# # defining useful function for input data collection
# def getInt(): return int(sys.stdin.readline().strip())
# def getStr(): return sys.stdin.readline().strip()
# def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
# def getStrSeq(): return sys.stdin.readline().strip().split()
# def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
# def getStrList(): return list(sys.stdin.readline().strip().split())


# # getting the input data
# n, s = getIntList()

# array = getIntList()

# currSum = 0

# left = 0

# window = 0

# for right in range(n):
#     currSum += array[right]

#     while currSum > s:
#         currSum -= array[left]
#         left += 1
    
#     window = max(window, right - left + 1)

# print(window)



"""
You are given an array of positive integers arr. Perform some operations (possibly none) 
on arr so that it satisfies these conditions:

The value of the first element in arr must be 1.
The absolute difference between any 2 adjacent elements must be less than or equal to 1. 
In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). 
abs(x) is the absolute value of x.
There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of arr to a smaller positive integer.
Rearrange the elements of arr to be in any order.
Return the maximum possible value of an element in arr after performing the operations to satisfy 
the conditions.

 

Example 1:

Input: arr = [2,2,1,2,1]
Output: 2
Explanation: 
We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
The largest element in arr is 2.
Example 2:

Input: arr = [100,1,1000]
Output: 3
Explanation: 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange arr so it becomes [1,100,1000].
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now arr = [1,2,3], which satisfies the conditions.
The largest element in arr is 3.

"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        currMax = 0

        for a in arr:
            if a > currMax + 1:
                a = currMax + 1
            
            currMax = a
        
        print(currMax)




if __name__ == '__main__':
    arr = [2,2,1,2,1]

    arr = [100,1,1000]

    Solution().maximumElementAfterDecrementingAndRearranging(arr)


