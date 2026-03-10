class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = 0
        maxSum = float('-inf')
        left = 0

        for right in range(len(nums)):

            windowSum += nums[right]

            if right - left + 1 == k:
                maxSum = max(windowSum, maxSum)

                windowSum -= nums[left]

                left += 1
        return maxSum/k