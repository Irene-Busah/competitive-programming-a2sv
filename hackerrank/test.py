from collections import Counter
from turtle import pos, position
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
You are given a string s and an integer array indices of the same length. The string s will be shuffled 
such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newString = list(s)

        for i in range(len(s)):
            pos = indices[i]

            newString[pos] = s[i]
        
        return ''.join(newString)





if __name__ == '__main__':
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]

    s = "abc"
    indices = [0,1,2]

    print(Solution().restoreString(s, indices))
