"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give 
each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child 
will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the 
cookie j to the child i, and the child i will be content. Your goal is to maximize the number 
of your content children and output the maximum number.


Example 1:
==========
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child 
whose greed factor is 1 content. You need to output 1.


Example 2:
========
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""

from typing import List


# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         left, right = 0, 0

#         g.sort()
#         s.sort()

#         count = 0

#         while left < len(g) and right < len(s):
#             if s[right] >= g[left]:
#                 count += 1

#                 left += 1
#                 right += 1
#             else:
#                 right += 1

#         print(count)




"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] 
and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or 
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Example 1:
==========
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
==========
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""


# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
#         pass





"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of 
pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 

Example 1:

Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
Example 2:

Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
Output: 10
"""


# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:

#         i, j = 0, len(nums)-1

#         nums.sort()

#         count = 0

#         while i < j:
#             if nums[i] + nums[j] < target:
#                 count += j - i
#                 i += 1
#             else:
#                 j -= 1
#         print(count)



"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s)-1

#         while i < j:
#             while i < j and not s[i].isalnum():
#                 i += 1
#             while i < j and not s[j].isalnum():
#                 j -= 1

#             if s[i].lower() != s[j].lower():
#                 return False
#             i+=1
#             j-=1        

#         return True




"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#         windowSum = 0
#         maxSum = float('-inf')
#         left = 0

#         for right in range(len(nums)):

#             windowSum += nums[right]

#             if right - left + 1 == k:
#                 maxSum = max(windowSum, maxSum)

#                 windowSum -= nums[left]

#                 left += 1
#         print(maxSum/k)



"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also 
correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = 0

#         lengthString = 0
#         window = set()

#         for right in range(len(s) - 1):
#             # windowSize += s[right]

#             while s[right] in window:
#                 window.remove(s[left])

#                 left += 1
            
#             window.add(s[right])
#             lengthString = max(lengthString, right - left + 1)
        
#         return lengthString



"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float('inf')

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closest - target):
                    closest = currentSum

                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return target


        return closest

if __name__  == '__main__':
    nums = [-1,2,1,-4]
    target = 1

    print(Solution().threeSumClosest(nums, target))
