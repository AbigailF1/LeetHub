class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        
        def dp(i,j):
            if i == len(triangle) - 1:
                memo[(i,j)] = triangle[i][j]
                return memo[(i,j)]
            
            if (i,j) not in memo:
                memo[(i,j)] += min(dp(i+1, j), dp(i+1, j+1)) + triangle[i][j]
                
            return memo[(i,j)]
        return dp(0,0)
        