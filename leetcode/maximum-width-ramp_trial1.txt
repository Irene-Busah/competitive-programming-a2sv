class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        # Step 1: build decreasing stack
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        ans = 0
        
        # Step 2: scan from right
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack[-1])
                stack.pop()
        
        return ans