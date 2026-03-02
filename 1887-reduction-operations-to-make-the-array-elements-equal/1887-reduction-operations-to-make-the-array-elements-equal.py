class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # initialize counter
        count = 0

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += len(nums) - i
        
        return count