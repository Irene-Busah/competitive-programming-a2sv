class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = Counter()
        players = set()

        for w, l in matches:
            players.add(w)
            players.add(l)
            loss[l] += 1

        zero_losses = [p for p in players if loss[p] == 0]
        one_loss = [p for p in players if loss[p] == 1]

        return [sorted(zero_losses), sorted(one_loss)]


