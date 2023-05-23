class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dic = {1:[[0,1],[0,-1]], 2:[[1,0], [-1,0]], 3:[[0,-1], [1,0]], 4:[[1,0], [0,1]], 5:[[-1,0],[0,-1]],6:[[-1,0],[0,1]]}
        direc = [(0,1), (1,0), (-1,0),(0,-1)]
        n = len(grid)
        m = len(grid[0])
        leng = (n*m) + 1
        rep = {}
        for i in range(n):
            for j in range(m):
                rep[(i,j)] = (i,j)
               
        def isvalid(x, y):
            if 0 <= x < n and 0<= y < m: return True
            return False    
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
        
            if x_rep != y_rep:
                rep[x_rep] = rep[y_rep]
                    
        
        for i in range(n):
            for j in range(m):
                for k in dic[grid[i][j]]:
                    x = i + k[0]
                    y = j + k[1]
                    if isvalid(x,y) and [-k[0], -k[1]] in dic[grid[x][y]]:
                        union((i,j),(x,y))
        
        x = find((0,0))
        y = find((n-1,m-1))
    
        if x != y:
            return False
        return True     
                      
                    
            
        