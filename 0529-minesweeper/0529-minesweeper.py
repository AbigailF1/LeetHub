class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direc = [(0,1), (0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        n = click[0]
        m = click[1]
        
        def isvalid(x, y):
            if 0 <= x < len(board) and 0<= y < len(board[0]): return True
            return False
        
        def ismine(x,y):
            if board[x][y] == "M": return True
            return False
            
        def dfs(n,m, visited): 
            visited.add((n,m))
            if ismine(n,m):
                return 
            mine = 0
            for i in direc:
                x = i[0] + n
                y = i[1] + m
                if isvalid(x,y) and (x,y) not in visited:
                    if ismine(x,y):
                        mine += 1
            if mine == 0:
                board[n][m] = "B"
                for i in direc:
                    x = i[0] + n
                    y = i[1] + m
                    if isvalid(x,y) and (x,y) not in visited:
                        dfs(x,y, visited)
            else:
                board[n][m] = str(mine)
                
        if board[n][m] == "M":
            board[n][m] = "X"
        else:
            dfs(n,m, set())
        return board
                
            
            
        