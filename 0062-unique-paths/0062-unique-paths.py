class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        graph = [[0] * (n + 1) for i in range(m)]
        graph[m -1][n-1] = 1
        
        direc = [(0,1), (1,0)]
        
        def isvalid(x,y):
            if 0 <= x < m and 0 <= y < n: return True
            else: return False
        
        for j in range(n -1, -1, -1):
            for i in range(m -1, -1, -1):
                for k in direc:
                    x = i + k[0]
                    y = j + k[1]
                    if isvalid(x,y):
                        graph[i][j] += graph[x][y]
        return graph[0][0]
        