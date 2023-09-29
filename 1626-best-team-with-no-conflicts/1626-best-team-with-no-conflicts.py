class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        
        scores_age = list(zip(scores,ages))
        scores_age.sort()
        
        # print(scores_age)
        memo = [scores_age[i][0] for i in range(n)]
        
        for i in range(n):
            score, age = scores_age[i]
        
            for j in range(i):
                    scorej, agej = scores_age[j]
                    if age >= agej:
                        memo[i] = max(memo[i] ,memo[j] + score)
        
        return max(memo)
            
            
        