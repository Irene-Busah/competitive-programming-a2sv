class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        newString = list(s)

        for i in range(len(s)):
            pos = indices[i]

            newString[pos] = s[i]
        
        return ''.join(newString)
        