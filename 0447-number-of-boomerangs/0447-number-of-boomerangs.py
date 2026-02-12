class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        
        for i in range(len(points)):
            distances = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx*dx + dy*dy 
                
                distances[dist] = distances.get(dist, 0) + 1
            
            for count in distances.values():
                total += count * (count - 1)
        
        return total        