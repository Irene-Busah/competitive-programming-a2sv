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
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the 
result be placed in the first part of the array nums. More formally, if there are k elements after 
removing the duplicates, then the first k elements of nums should hold the final result. It does not 
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.



Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums 
being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        
        
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: int
        """


if __name__ == '__main__':
   nums = [1,1,1,2,2,3]
   

   Solution().removeDuplicates(nums)
