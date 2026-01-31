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
