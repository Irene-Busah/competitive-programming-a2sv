class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        currSum = 0
        maxScore = 0
        seen = set()

        left = 0

        for right in range(len(nums)):

            while nums[right] in seen:
                seen.remove(nums[left])
                currSum -= nums[left]
                left += 1
            seen.add(nums[right])
            currSum += nums[right]

            maxScore = max(currSum, maxScore)
        return maxScore
        