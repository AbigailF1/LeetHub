class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        
        def inbound(x, y):
            return 0<=x<n and 0<=y<m        
        
        def bfs():
            h = [(0,0,0)]

            visited = set()
            
            while h:
                obs,i,j = heapq.heappop(h)
                
                if i == n-1 and j == m-1:
                    return obs
                
                if (i, j) not in visited:
                    visited.add((i,j))
                    for x, y in directions:
                        nx, ny = x+i, y+j
                        if inbound(nx, ny):
                            diff = obs + grid[i][j]
                            heapq.heappush(h, (diff,nx,ny))
        
        
        return bfs()
        