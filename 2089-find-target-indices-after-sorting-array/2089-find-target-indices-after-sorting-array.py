class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arraySize = len(nums)

        res = []

        for i in range(arraySize):
            for j in range(arraySize-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        for i in range(arraySize):
            if nums[i] == target:
                res.append(i)
        
        return res