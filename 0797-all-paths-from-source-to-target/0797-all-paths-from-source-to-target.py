class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans =[]
        n = len(graph)
        queue = deque()
        queue.append([[0], 0])
        
        while queue:
            res, node = queue.popleft()
            if node == n-1:
                ans.append(res)
            for i in graph[node]:
                queue.append([res+ [i], i])
        return ans
            
            
        