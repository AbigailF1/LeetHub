class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def isvalid(x, y):
            if 0 <= x < m and 0<= y < n  and board[x][y] == "O": return True
            return False
        
        def boarder(x,y):   
            if (x == 0 or x == m -1 or y == 0 or y == n-1) and board[x][y] == "O": return True
            return False
        
        def dfs(m,n):
            if isvalid(m,n):
                board[m][n] = "1"
                for i in direc:
                    x = i[0] + m
                    y = i[1] + n
                    dfs(x,y)
             
        for i in range(m):
            for j in range(n):
                if boarder(i,j):
                    dfs(i,j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "1":
                    board[i][j] = "O"
                    
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
        return board
                
            
        