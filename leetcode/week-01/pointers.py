"""
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


from itertools import count
from typing import Counter, List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         left = 0
        

#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[left], nums[right] = nums[right], nums[left]
    
#                 left += 1
        
#         print(nums)




"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete 
in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest 
score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each 
athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., 
the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:
==========
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
==========
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""


# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         sortedScores = sorted(score, reverse=True)

#         rank = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

#         scoreToRank = {}

#         for i in range(len(score)):
#             placement = i+1
#             if placement in rank:
#                 scoreToRank[sortedScores[i]] = rank[placement]
#             else:
#                 scoreToRank[sortedScores[i]] = str(placement)

#         res = []
#         for s in score:
#             res.append(scoreToRank[s])
#         print(res)



"""
You are given an integer num. Rearrange the digits of num such that its value is minimized and 
it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

Example 1:
==========
Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.

Example 2:
==========
Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
"""

# class Solution:
#     def smallestNumber(self, num: int) -> int:
#         digit_list = [int(d) for d in str(abs(num))]
#         if num > 0:
#             digit_list.sort()

#             count = 0
#             for i in range(len(digit_list)):
#                 if digit_list[i] == 0:
#                     count += 1
            
#             digit_list[0], digit_list[count] = digit_list[count], digit_list[0]

#             print(int("".join(str(d) for d in digit_list)))
#         else:
#             digit_list.sort(reverse=True)
#             val = "".join(str(d) for d in digit_list)
            
#             print(int("-" + val))



"""
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

 

Example 1:
=========
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
=========
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
=========
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""
       

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:

#         newArray = list(set(nums))

#         newArray.sort(reverse=True)

#         if len(nums) >= 3:
#             print(newArray[2], newArray)
#         else:
#             print(max(newArray), newArray)
#         # print(nums)





"""
You are given a 0-indexed integer array players, where players[i] represents the ability of 
the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] 
represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or 
equal to the trainer's training capacity. Additionally, the ith player can be matched 
with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

 

Example 1:
==========
Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.


Example 2:
==========
Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.

"""


# class Solution:
#     def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
#         # sorting the array
#         players.sort()
#         trainers.sort()

#         first = 0
#         second = 0

#         count = 0

        
#         while first < len(players) and second < len(trainers):
#             if trainers[second] >= players[first]:
#                 count += 1

#                 first += 1
#                 second += 1
#             else:
#                 second += 1

#         print(count)




"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and 
remove them from the array.

Return the maximum number of operations you can perform on the array.


Example 1:
==========
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


Example 2:
=========
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1

        count = 0

        while left < right:
            val = nums[left] + nums[right]

            if val == k:
                count += 1
                left += 1
                right -= 1
            elif val < k:
                left += 1
            else:
                right -= 1

            

        print(count)

if __name__ == '__main__':
    nums = [1,2,3,4]
    k = 5
    Solution().maxOperations(nums, k)

