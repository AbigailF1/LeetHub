class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        n, m = len(grid), len(grid[0])
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m
        direc = [(0,1) ,(1,0), (-1,0), (0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for x, y in direc:
                        nx, ny = i + x, j + y
                        if not is_valid(nx, ny) or grid[nx][ny] == 0:
                            perim += 1
        return perim         


        