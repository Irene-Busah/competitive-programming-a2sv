class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The time and space complexity of this algorithm is O(n)

        # First we can create an empty dictionary
        hashmap = {}

        # then, loop through the list to find the values which added together, will give
        # the target. We can achieve that by subtracting the current value from the target
        for i in range(len(nums)):
            x = target - nums[i]
            # if x is the dictionary, we will return the index of the current element and the 
            # value of the x in the dictionary
            if x in hashmap:
               return [hashmap[x], i]

            # else, we add the current element and its index
            hashmap[nums[i]] = i
        