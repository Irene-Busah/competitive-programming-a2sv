class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        right = 1
        for left in range(1, len(nums)):
            if nums[left] != nums[right - 1]:
                nums[right] = nums[left]
            
                right += 1

        del nums[right:] 

        return len(nums)
        