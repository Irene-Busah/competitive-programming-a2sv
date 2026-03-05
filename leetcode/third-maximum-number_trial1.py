class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        newArray = list(set(nums))

        newArray.sort(reverse=True)

        if len(nums) >= 3:
            return newArray[2]
        else:
            return max(newArray)