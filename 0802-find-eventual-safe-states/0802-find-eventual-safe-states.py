class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph2 = [[] for _ in range(len(graph))]
        
        incoming = [0 for _ in range(len(graph))]
        queue = deque()
        ans = []
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                incoming[i] += 1
                graph2[graph[i][j]].append(i)
            
        for i in range(len(graph2)):
            if incoming[i] == 0:
                queue.append(i)
        print(graph) 
        print(graph2)        
        while queue:
            ans.append(queue.popleft())
            
            for neighbour in graph2[ans[-1]]:
                incoming[neighbour] -= 1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        
        return sorted(ans)
        