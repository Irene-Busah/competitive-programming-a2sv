class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def can_ship(cap):
            days_used = 1
            current = 0
            
            for w in weights:
                if current + w > cap:
                    days_used += 1
                    current = 0
                current += w
            
            return days_used <= days
        
        while left < right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        
        return left