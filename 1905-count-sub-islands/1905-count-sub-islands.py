class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direc = [(0,1), (1,0), (-1,0), (0,-1)]
        n = len(grid1)
        m = len(grid1[0])
        
        def isvalid(x,y):
            return 0 <= x < n and 0 <= y < m
        is_found = True
        
        # visited = set()
        def dfs(row, col):
            nonlocal is_found
            if grid2[row][col] != grid1[row][col]:
                is_found = False
            grid2[row][col] = 0
            for i, j in direc:
                x = i + row
                y = j + col
                if isvalid(x, y) and grid2[x][y] == 1:
                    dfs(x, y)   
      
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    is_found = True
                    dfs(i,j)
                    ans += is_found
        return ans
            
            
        
        