class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        row, col = len(mat), len(mat[0])
        queue = deque()
        ans = [[0 for j in range(col)] for i in range(row)]
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append([i,j,0])
        while queue:
            r,c,path = queue.popleft()
            for i, j in direc:
                x, y = i + r, j + c
                if (x, y) not in visited and 0 <= x < row and 0 <= y < col:
                    ans[x][y] = path+1
                    queue.append([x,y,ans[x][y]])
                    visited.add((x,y))
            
        return ans