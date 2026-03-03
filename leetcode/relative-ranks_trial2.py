class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = sorted(score, reverse=True)

        rank = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

        scoreToRank = {}

        for i in range(len(score)):
            placement = i+1
            if placement in rank:
                scoreToRank[sortedScores[i]] = rank[placement]
            else:
                scoreToRank[sortedScores[i]] = str(placement)

        res = []
        for s in score:
            res.append(scoreToRank[s])
        return res