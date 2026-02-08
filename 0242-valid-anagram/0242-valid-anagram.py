class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        counter_s = Counter(s)

        counter_t = Counter(t)

        return counter_s == counter_t