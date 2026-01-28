class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Steps:

        Set prefix = strs[0]

        For each string:

        While the string does not start with prefix, remove the last character of prefix

        When done, prefix is the answer
        
        """
        
        if not strs:
            return ""
        
        prefix = strs[0]

        # moving through the list
        for i in range(len(strs) - 1):
            while not strs[i + 1].startswith(prefix):
                prefix = prefix[:-1]
        return prefix