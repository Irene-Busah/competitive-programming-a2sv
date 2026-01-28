class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Returns the maximum product of three numbers in the list.

        Example: [-19, -18, 3, 4]
        """

        # initialize the product
        product = 0

        # counting the negatives and positives
        negatives = 0
        positives = 0

        # going through the list
        for num in nums:
            if num < 0:
                negatives += 1
            else:
                positives += 1
        
        # sorting the list
        newList = sorted(nums)

        # If there are no positives (all negatives), take the top 3 (closest to 0)
        if positives == 0:
            product = newList[-1] * newList[-2] * newList[-3]
            return product

        # Otherwise, consider the "two smallest * largest" option if possible
        if negatives >= 2:
            product = newList[0] * newList[1] * newList[-1]

        # And also consider the "top 3" option if possible
        if positives >= 3:
            product = max(product, newList[-1] * newList[-2] * newList[-3])
        
        return product

