class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # counting the elements
        list_count = Counter(nums)

        # going through the list
        # for num in nums:
        #     if num in list_count.keys():
        #         list_count[num] += 1
        #     else:
        #         list_count[num] = 1
        
        for val in list_count.values():
            if val >= 2:
                return True

        return False


        