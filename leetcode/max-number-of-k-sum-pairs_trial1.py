class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1

        count = 0

        while left < right:
            val = nums[left] + nums[right]

            if val == k:
                count += 1

            left += 1
            right -= 1

        return count