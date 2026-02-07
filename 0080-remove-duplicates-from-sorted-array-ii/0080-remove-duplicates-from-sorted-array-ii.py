class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Returns duplicates
        
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: int
        """

        counter = 0

        for num in nums:
            if counter < 2 or num != nums[counter - 2]:
                nums[counter] = num

                counter += 1
        
        return counter
        

