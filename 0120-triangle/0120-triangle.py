class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        memo = [[inf] * (n -1) for _ in range(n -1)]
        memo.append(triangle[-1])
        
        for i in range(n -2, -1, -1):
            for j in range(i, -1, -1):
                memo[i][j] = min(memo[i+1][j], memo[i+1][j+1]) + triangle[i][j]
        # print(memo)        
        return memo[0][0]
        