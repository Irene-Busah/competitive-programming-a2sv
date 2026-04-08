class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Compute next greater for each number in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # For elements that have no next greater
        while stack:
            prev = stack.pop()
            next_greater[prev] = -1

        # Build result for nums1
        return [next_greater[num] for num in nums1]