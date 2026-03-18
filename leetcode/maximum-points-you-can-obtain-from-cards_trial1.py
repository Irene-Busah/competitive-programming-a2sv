class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints)-1

        max_score = 0
        move = 0

        while left <= right and move < k:
            if cardPoints[left] > cardPoints[right]:
                max_score += cardPoints[left]
                move += 1
                left += 1
            else:
                max_score += cardPoints[right]
                move += 1
                right -= 1

        return max_score