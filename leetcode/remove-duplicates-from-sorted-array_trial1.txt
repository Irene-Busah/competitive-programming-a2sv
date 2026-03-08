class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # APPROACH 1

        right = 1
        for left in range(1, len(nums)):
            if nums[left] != nums[right - 1]:
                nums[right] = nums[left]
            
                right += 1

        del nums[right:] 

        # APPROACH 2

        # setting the left index
        # left = 0

        # # go through the list
        # while left < len(nums) - 1:
        #     if nums[left] == nums[left + 1]:
        #         nums.pop(left)
        #     else:
        #         left += 1

        return len(nums)
        