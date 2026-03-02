class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}

        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1
        
        res = [v*k for k, v in sorted(counter.items(), key=lambda x: -x[1])]

        return "".join(res)