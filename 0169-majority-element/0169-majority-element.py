class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counting each element in the list
        counter = Counter(nums)

        majority_ele = 0

        for key, val in counter.items():
            if val > len(nums)/2:
                majority_ele = key

        return majority_ele
        