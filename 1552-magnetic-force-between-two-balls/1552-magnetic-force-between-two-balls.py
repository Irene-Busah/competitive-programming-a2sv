class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        left = 1
        right = position[-1] - position[0]
        
        def can_place(dist):
            count = 1
            last = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last >= dist:
                    count += 1
                    last = position[i]
                
                if count == m:
                    return True
            
            return False
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_place(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right