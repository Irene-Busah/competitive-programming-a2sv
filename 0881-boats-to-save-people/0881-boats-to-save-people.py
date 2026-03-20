class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        [3,2,2,1]
        Sort: [1,2,2,3]

        count = 1 2 3
        left: 1 2
        right: 3 2

        [3,5,3,4] -> 5
        sort: [3,3,4,5]
        count = 1 2
        left = 3
        right = 5 4 3
        """
        people.sort()

        count = 0

        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            
            elif people[right] <= limit:
                count += 1
                right -= 1
            else:
                count += 1
                left += 1
        
        return count
        