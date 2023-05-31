class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        graph = [[0] * (n + 1) for i in range(m)]
        graph[m -1][n-1] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    graph[i][j] = -1
                
        direc = [(0,1), (1,0)]
        
        def isvalid(x,y):
            if 0 <= x < m and 0 <= y < n and graph[x][y]!= -1: return True
            else: return False
        
        for j in range(n -1, -1, -1):
            for i in range(m -1, -1, -1):
                for k in direc:
                    x = i + k[0]
                    y = j + k[1]
                    if isvalid(x,y) and isvalid(i,j):
                        graph[i][j] += graph[x][y]
        x = graph[0][0]
        if x != -1:
            return x
        else:
            return 0
        