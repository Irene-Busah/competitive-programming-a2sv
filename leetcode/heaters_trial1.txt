class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            
            left_dist = float('inf')
            right_dist = float('inf')
            
            if i > 0:
                left_dist = house - heaters[i - 1]
            if i < len(heaters):
                right_dist = heaters[i] - house
            
            res = max(res, min(left_dist, right_dist))
        
        return res