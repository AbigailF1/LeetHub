class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0 for _ in range(len(graph))]
        for i in range(len(edges)):
            indegree[edges[i][1]] += 1
            graph[edges[i][0]].append(edges[i][1])
        
        queue = deque()
        ans = [set() for i in range(n)]
        
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)
                
        
        while queue:
            x = queue.popleft()
            for neighbour in graph[x]:
                ans[neighbour].add(x)
                if ans[x]!= []:
                    for i in ans[x]:
                        ans[neighbour].add(i)
                indegree[neighbour] -= 1
                
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        for i in range(n):
            ans[i] = sorted(list(ans[i]))       
            
        
        return  ans
            
        