from collections import Counter
from typing import List


# class Solution:
#     def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#         loss = Counter()
#         players = set()

#         for w, l in matches:
#             print(w, l)
#             players.add(w)
#             players.add(l)
#             loss[l] += 1

#         zero_losses = [p for p in players if loss[p] == 0]
#         one_loss = [p for p in players if loss[p] == 1]

#         return [sorted(zero_losses), sorted(one_loss)]
    

# if __name__ == '__main__':
#     matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
#     print(Solution().findWinners(matches))



# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         results = []
#         counters = []
#         for i in range(len(words)):
#             counter = Counter(words[i])
#             counters.append(counter)
        
#         for key in counters[0]:
#             min_count = min(counter.get(key, 0) for counter in counters)

#             if min_count > 0:
#                 results.extend([key] * min_count)
#         print(results)
        



# if __name__ == '__main__':
#     words = ["bella","label","roller"]
#     Solution().commonChars(words)




"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, 
excluding the space needed to store the output

 

Example 1:
==========
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
==========
Input: nums = [1,1,2]
Output: [1]

Example 3:
==========
Input: nums = [1]
Output: []

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                res.add(nums[i])
            else:
                seen.add(nums[i])
        
        print(res, seen)




if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]

    nums = [1,1,2]

    nums = [1]

    nums = [3,11,8,16,4,15,4,17,14,14,6,6,2,8,3,12,15,20,20,5]

    Solution().findDuplicates(nums)
