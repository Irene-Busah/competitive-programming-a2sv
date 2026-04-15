class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # base case
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)
        
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):
            row[i] = prev[i - 1] + prev[i]
        
        return row