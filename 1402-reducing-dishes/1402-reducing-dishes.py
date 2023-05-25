class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        new = sorted(satisfaction, reverse = True)
        n = len(satisfaction)
        maxx = 0
        summ = 0
        for i in new:
            if summ + i > 0:
                summ += i
                maxx += summ
                # print(maxx, summ)
        return maxx
                
                
            
        