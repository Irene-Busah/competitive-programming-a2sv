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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        window = set()

        left = 0

        for right in range(len(s)):
            

            while s[right] in window:
                window.remove(s[left])
                
                left += 1
            window.add(s[right])
            res = max(res, right - left + 1)
        
        return res





if __name__ == '__main__':
    s = "abcabcbb"

    print(Solution().lengthOfLongestSubstring(s))


