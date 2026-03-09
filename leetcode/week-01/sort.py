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

from itertools import count
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


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:




if __name__  == '__main__':
    g = [1,2,3]
    s = [1,1]

    g = [1,2]
    s = [1,2,3]

    Solution().findContentChildren(g, s)
