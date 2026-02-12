class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        """
        The key important part of the problem is computing the distance between each ghost and the target and the actual target distance 
        """

        distance = abs(target[0]) + abs(target[1])

        # possible = None
        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance <= distance:
                return False
        return True