class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [0] * n
        memo[-1] = questions[-1][0]
        
        for i in range(n-2, -1,-1):
            target = questions[i][1] + 1 + i 
            if target < n:
                memo[i] = max(memo[i + 1] , questions[i][0] + memo[target])
            else:
                memo[i]= max(memo[i + 1], questions[i][0])
        return memo[0]
        