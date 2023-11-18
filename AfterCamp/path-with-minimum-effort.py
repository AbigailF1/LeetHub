class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        def is_valid(x,y):
            return 0 <= x < n and 0 <= y < m

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        effort = float("-inf")
        # bfs 
        heap = [(0,0,0)]
        visited = set()

        while heap:
            effort , i, j = heappop(heap)
            if (i,j) == (n-1,m-1):
                return effort 
            if (i,j) not in visited:
                visited.add((i,j))
                for x, y in directions:
                    nx , ny = i + x, j + y
                    if is_valid(nx, ny):
                        curr_effort = max(effort,  abs(heights[i][j] - heights[nx][ny]))
                        heappush(heap, (curr_effort, nx, ny))
