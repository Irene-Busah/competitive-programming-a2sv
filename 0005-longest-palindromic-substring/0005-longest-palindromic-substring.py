class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Palindrome reads characters same forward and backward. The substring can be even or dd

        Observation
        -----------


        """

        longest = ""
        n = len(s)

        def expand(left, right):
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]

        
        for i in range(n):

            odd = expand(i, i)

            if len(odd) > len(longest):
                longest = odd

            even = expand(i, i + 1)

            if len(even) > len(longest):
                longest = even

        return longest 
        