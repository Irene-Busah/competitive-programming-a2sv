class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        if len(p) > len(s):
            print(res)

        counter_p = Counter(p)
        window = Counter()

        lenOfP = len(p)

        for i in range(len(s)):
            window[s[i]] += 1

            if i >= lenOfP:
                if window[s[i-lenOfP]] == 1:
                    del window[s[i-lenOfP]]
                else:
                    window[s[i-lenOfP]] -= 1
            
            if window == counter_p:
                res.append(i-lenOfP+1)
            
        return res