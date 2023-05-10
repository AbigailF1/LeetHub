class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for i in range(n-2)] for j in range (n-2)]
        
        for i in range(len(ans)):
            for j in range(len(ans)):
                maxx = 0
                for r in range(i,i+3):
                    for c in range (j,j+3):
                        maxx = max(maxx, grid[r][c])
                ans[i][j] = maxx 
                
                
        return ans
        