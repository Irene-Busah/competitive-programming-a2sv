class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # set the counter
        count = 0

        # going through array
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1

        return count
        