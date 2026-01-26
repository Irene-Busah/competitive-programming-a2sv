class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        Returns the smallest positive integer that is a multiple of 2 and n
        """

        smallest_value = 0

        # if n is odd, smallest value -> n * 2
        if (n % 2 != 0 ):
            smallest_value = n * 2
        # otherwise, the smallest value is n
        else:
            smallest_value = n
        
        return smallest_value

