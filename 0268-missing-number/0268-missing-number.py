class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Loop through the range and at each value, we can check if it is the list. If it is not, we return the value
        """

        # setting the missing number
        missing_val = 0

        # looping through the range, n, to find the missing value
        for i in range(len(nums) + 1):
            if i not in nums:
                missing_val = i
        
        return missing_val

        


