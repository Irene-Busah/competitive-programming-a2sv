class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        For this problem, we will use two pointers - one at the start and the other at the end of the list.

        At each step, we store the maximum amount of water after computing the area

        height = [1, 7, 2, 5, 4, 7, 3, 6]

        i = 1, 7, 2, 5, 4
        j = 6, 3, 7

        res = (7-0) * 1 = 7
            = (7-1) * 6 = 36
            = (6-1) * 3 = 15
            = (5-1) * 7 = 28
            = (5-2) * 2 = 6
            = (5-3) * 5 = 10
            = (5-4) * 4 = 4
        """

        # initializing the final results
        max_amount = 0

        # initialing the two pointers
        left, right = 0, len(height) - 1

        while left < right:

            # computing the maximum water for the container
            res = (right - left) * min(height[right], height[left])

            # checking if the current maximum is smaller than the computed max container
            if res > max_amount:
                max_amount = res
            
            # checking 
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_amount