class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = [val for val, count in counter.items() if count > len(nums)/3]

        return res