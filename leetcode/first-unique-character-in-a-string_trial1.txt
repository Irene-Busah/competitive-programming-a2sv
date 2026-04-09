class Solution:
    def firstUniqChar(self, s: str) -> int:

        # newS = s

        d = deque()

        mapper = {}

        # print(s.index('o'))

        for i in range(len(s)):
            if s[i] not in mapper:
                mapper[s[i]] = 1
            else:
                mapper[s[i]] += 1
        
        for ch in s:
            if mapper[ch] == 1:
                d.append(ch)
                
        if d:
            ele = s.index(d.popleft())
            return ele
        else:
            return -1