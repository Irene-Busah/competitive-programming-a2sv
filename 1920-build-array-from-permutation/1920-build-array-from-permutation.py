class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Returns the Permutation of the input list
        """

        newList = []

        for i in range(len(nums)):
            newList.append(nums[nums[i]])

        return newList