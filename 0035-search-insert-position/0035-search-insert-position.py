class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        """
        Returns the index of the target value in the array
        
        :param self: Description
        :param nums: input array
        :type nums: List[int]
        :param target: target value 
        :type target: int
        :return: index of target value
        :rtype: int
        """

        left = 0
        right = len(nums)

        idx = -1
        while left < right:
            mid = (left + right) // 2

            # checking if the target is less than the mid value
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            
            if nums[mid] == target:
                idx = mid
            if left == right:
                idx = left
        
        return idx
        