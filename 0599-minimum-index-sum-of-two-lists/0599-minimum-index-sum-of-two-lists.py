class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        pos = {}
        least_index = float('inf')
        res = []
        for i, val in enumerate(list2):
            pos[val] = i


        for i, x in enumerate(list1):
            if x in pos:
                index = pos[x] + i
                if index < least_index:

                    least_index = index
                    res = [x]
                elif index == least_index:
                    res.append(x)
        
        return res