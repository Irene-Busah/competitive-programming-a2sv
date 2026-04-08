
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
        if len(stack) == 0:
            return ""
        else:
            return "".join(stack)

        