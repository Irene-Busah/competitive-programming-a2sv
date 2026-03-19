class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        nums = [23,2,4,6,7], k = 6

        42
        """
        total = 0

        remainder_mapper = {0: -1}

        for i in range(len(nums)):
            total += nums[i]
            reminder = total % k

            if reminder in remainder_mapper:
                if i - remainder_mapper[reminder] >= 2:
                    return True
            else:
                remainder_mapper[reminder] = i
            
        return False





        # total = sum(nums)
        # left = 0

        # for right in range(len(nums)):
        #     if total % k == 0:
        #         return True
            
        #     else:
        #         total -= nums[left]
        #         left += 1


        
        return False



