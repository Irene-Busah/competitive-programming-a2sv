class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        currMax = 0

        for a in arr:
            if a > currMax + 1:
                a = currMax + 1
            
            currMax = a
        
        return currMax