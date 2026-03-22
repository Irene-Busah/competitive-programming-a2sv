class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        maxWindow = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > n - 1:
                left += 1
            
            maxWindow = max(maxWindow, right - left + 1)
        
        return n - maxWindow