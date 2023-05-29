class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        direc = [[1,0],[0,1],[-1,0],[0,-1]]
        rep = {}
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                rep[(i,j)] = (i,j)
        matrix = [[0] * col for i in range(row)]
        
        def find(x):
            if x != rep[x]:
                rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            x_rep = find(x)
            y_rep = find(y)
            
            if (x_rep[0] == 1 and y_rep[0] == row) or (x_rep[0] == row and y_rep[0] == 1):
                return True
            if x_rep[0] == 1 or x_rep[0] == row:
                rep[y_rep] = x_rep
            else:
                rep[x_rep] = y_rep
            return False
                
        def is_valid(x,y):
            if 0 <= x < row and 0 <= y < col and matrix[x][y]==1:
                return True
            else:
                return False
                
        for k in range(len(cells)-1,-1,-1):
            r,c = cells[k][0]-1 , cells[k][1]-1
            matrix[r][c] = 1
            for i,j in direc:
                x,y = r + i, c + j
                flag = False
                if is_valid(x,y):
                    flag= union((x+1,y+1),(r+1,c+1))
                if flag: 
                    return k