class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1), (1,1), (-1,-1), (1,-1), (-1, 1)]
        n = len(grid) - 1
        if grid[0][0] or grid[n][n]:
            return -1
        queue = deque()
        queue.append([(0,0), 1])
        visited = set()
        visited.add((0,0))
        
        ans = inf
        while queue:
            (r,c), path = queue.popleft()
            if r == n and c == n:
                ans = min(ans, path)
                continue
            for i, j in direc:
                x, y = i + r, j + c
                if (x, y) not in visited and 0 <= x <= n and 0 <= y <= n and grid[x][y]==0:
                    queue.append([(x,y), path+1])
                    visited.add((x,y))
        if ans == inf:
            return -1
        return ans 
            