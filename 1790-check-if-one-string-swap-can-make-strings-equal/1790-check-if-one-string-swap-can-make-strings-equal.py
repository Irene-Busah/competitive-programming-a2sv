class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))

        if len(diff) == 0:
            return True

        if len(diff) == 2:
            return diff[0] == diff[1][::-1]

        return False