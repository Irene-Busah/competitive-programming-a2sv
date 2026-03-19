class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        window = {}

        left = 0

        ans = 0
        pairs = 0

        for right in range(len(nums)):
            pairs += window.get(nums[right], 0)
            window[nums[right]] = window.get(nums[right], 0) + 1


            while pairs >= k:
                ans += len(nums) - right
            
                window[nums[left]] -= 1
                pairs -= window[nums[left]]
                left += 1

        return ans