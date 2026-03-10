class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float('inf')

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closest - target):
                    closest = currentSum

                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return target

        return closest
        
        