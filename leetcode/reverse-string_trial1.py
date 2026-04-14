class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        """
        Recursion approach

        if len(s) == 0 or len(s) == 1:
            return s

        return self.reverseString(s[1:]) + [s[0]]
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
        return s

        