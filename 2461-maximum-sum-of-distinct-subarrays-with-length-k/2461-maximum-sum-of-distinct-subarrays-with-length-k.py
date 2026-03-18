class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:


        left = 0
        window = {}
        total = 0
        count = 0

        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right], 0) + 1
            total += nums[right]

            if right - left + 1 > k:
                window[nums[left]] -= 1

                if window[nums[left]] == 0:
                    del window[nums[left]]
                
                total -= nums[left]
                left += 1
            
            if right - left + 1 == k and len(window) == k:
                count = max(count, total)
        
        return count


        