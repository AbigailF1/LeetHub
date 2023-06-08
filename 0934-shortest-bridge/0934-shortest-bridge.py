class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        queue = deque()
        visited = set()
        for i in range(n):
            if len(queue) > 0:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
                    break
        queue2 = deque()            
        while queue:
            (r,c) = queue.popleft()
            visited.add((r,c))
            queue2.append((r,c))
            for i, j in direc:
                x, y = i + r, j + c
                if (x, y) not in visited and 0 <= x < n and 0 <= y < n and grid[x][y]==1:
                    queue.append((x,y))
                    visited.add((x,y))
        ans = 0
        while queue2:
            for _ in range(len(queue2)):
                (r,c) = queue2.popleft()
                for i, j in direc:
                    x, y = i + r, j + c
                    if (x, y) not in visited and 0 <= x < n and 0 <= y < n and grid[x][y]==0:
                        queue2.append((x,y))
                        visited.add((x,y))
                    if (x, y) not in visited and 0 <= x < n and 0 <= y < n and grid[x][y]==1:
                        return ans
            ans += 1


