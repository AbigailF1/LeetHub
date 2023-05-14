class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        possible = skill[0] + skill[-1]
        ans = 0
        # print(skill)
        for i in range(int(len(skill)/2)):
            if skill[i] + skill[-(i+1)]!= possible:
                return -1
            else:
                ans += skill[i] * skill[-(i+1)]
        return ans
                
            
        