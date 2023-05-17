class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph2 = [[] for _ in range(numCourses)]
        prereq = [0] * numCourses
        visited = defaultdict(set)
        for dep , notd in prerequisites:
            graph2[notd].append(dep)
            prereq[dep] += 1
        
        queue = deque()

        ans = []
        for i in range(numCourses):
            if prereq[i] == 0:
                queue.append(i)

        while queue:
            x = queue.popleft()
            for i in graph2[x]:
                prereq[i] -= 1
                for j in visited[x]:
                    visited[i].add(j)
                visited[i].add(x)
                if prereq[i] == 0:
                     queue.append(i)
        for i, j in queries:
            if j in visited[i]:
                ans.append(True)
            else:
                ans.append(False)
                    
                    
        return ans
        