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
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and
 list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:
==========
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey 
Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".


Example 2:
==========
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        pass



if __name__ == '__main__':
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

    Solution().findRestaurant(list1, list2)
