class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        skillTotal = sum(skill)
        teams = len(skill) // 2

        if skillTotal % teams != 0:
            return -1

        res = 0
        teamSum = skillTotal // teams
            
        
        left, right = 0, len(skill)-1

        while left < right:
            if skill[left] + skill[right] != teamSum:
                return -1
            res += skill[left] * skill[right]

            left += 1
            right -= 1

        return res