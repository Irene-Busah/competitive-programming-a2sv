class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []

        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            res.append(currSum)
        
        return res