class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We are given a string, s, and a target, k.
        The goal is to return the longest substring
        after choosing k elements to replace.

        We use a sliding window to find the longest substring where we can replace at most 
        k characters to make all characters the same.

        We maintain a frequency map of characters in the window and track the count of the 
        most frequent character.

        If the window size minus the max frequency exceeds k, we shrink the window from the 
        left.

        Otherwise, we update the maximum window length.
        """

        left = 0
        count = {}
        max_count = 0
        results = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            

            results = max(results, right - left + 1)
        
        return results