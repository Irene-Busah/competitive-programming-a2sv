class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        removedItems = []
        
        while nums[0]:
            roundMax = []
            for i in range(len(nums)):
                nums[i].sort()
                maxValue = nums[i].pop()

                roundMax.append(maxValue)

            removedItems.append(max(roundMax))
            
        return sum(removedItems)

        