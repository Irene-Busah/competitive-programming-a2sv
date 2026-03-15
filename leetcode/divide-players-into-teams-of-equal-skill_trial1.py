class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        skillTotal = sum(skill)
        teams = len(skill) / 2

        res = 0

        teamSum = skillTotal / teams
            
        
        left, right = 0, len(skill)-1

        while left < right:
            if skill[left] + skill[right] == teamSum:
                res += skill[left] * skill[right]
            else:
                res = -1

            left += 1
            right -= 1

        return res