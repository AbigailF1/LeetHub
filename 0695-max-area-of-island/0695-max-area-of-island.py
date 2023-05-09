class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        def dfs(i, j):
            if (i, j) in visited or i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0]) or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            area = grid[i][j]
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            return area 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    ans = max(ans, dfs(i,j))
        return ans
                    
        
        
        