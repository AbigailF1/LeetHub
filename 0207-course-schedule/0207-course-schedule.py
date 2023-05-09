class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        ans = []
        
        for dep , notd in prerequisites:
            incoming[dep] += 1
            graph[notd].append(dep)
            
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            ans.append(queue.popleft())
            for neighbour in graph[ans[-1]]:
                incoming[neighbour] -= 1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        if len(ans) < numCourses:
            return False
        
        return True