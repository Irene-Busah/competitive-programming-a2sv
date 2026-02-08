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
Given an integer array nums of length n, you want to create an array ans of length 2n where 
ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums

        print(ans)

if __name__ == '__main__':
   nums = [1,2,1]
   nums = [1,3,2,1]


   Solution().getConcatenation(nums)
