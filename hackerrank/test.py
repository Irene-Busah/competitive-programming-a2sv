from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = Counter()
        players = set()

        for w, l in matches:
            print(w, l)
            players.add(w)
            players.add(l)
            loss[l] += 1

        zero_losses = [p for p in players if loss[p] == 0]
        one_loss = [p for p in players if loss[p] == 1]

        return [sorted(zero_losses), sorted(one_loss)]
    

if __name__ == '__main__':
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    print(Solution().findWinners(matches))



class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        results = []
        counters = []
        for i in range(len(words)):
            counter = Counter(words[i])
            counters.append(counter)
        
        for key in counters[0]:
            min_count = min(counter.get(key, 0) for counter in counters)

            if min_count > 0:
                results.extend([key] * min_count)
        print(results)
        



if __name__ == '__main__':
    words = ["bella","label","roller"]
    Solution().commonChars(words)




"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

