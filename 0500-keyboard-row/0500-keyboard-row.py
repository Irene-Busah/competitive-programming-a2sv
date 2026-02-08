class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        
        # first row of the keyboard
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"

        res = []

        for word in words:
            w = word.lower()
            if w[0] in firstRow:
                row = firstRow
            elif w[0] in secondRow:
                row = secondRow
            else:
                row = thirdRow
            
            valid = True
            for ch in w:
                if ch not in row:
                    valid = False
                    continue
            
            if valid:
                res.append(word)
        
        return res

