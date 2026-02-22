class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballColor = {}  # maps ball -> color
        colorCount = {}  # maps color -> count of balls with that color
        result = []

        for x, y in queries:
            # If ball x already has a color, remove it from that color's count
            if x in ballColor:
                oldColor = ballColor[x]
                colorCount[oldColor] -= 1
                if colorCount[oldColor] == 0:
                    del colorCount[oldColor]
            
            # Assign new color to ball x
            ballColor[x] = y
            colorCount[y] = colorCount.get(y, 0) + 1
            
            # Number of distinct colors = size of colorCount
            result.append(len(colorCount))
        
        return result
        

