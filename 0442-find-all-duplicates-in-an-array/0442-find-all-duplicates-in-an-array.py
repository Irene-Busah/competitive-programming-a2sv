class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                res.append(nums[i])
                # seen.pop()
            else:
                seen.append(nums[i])
        seen.clear()
        return res
        