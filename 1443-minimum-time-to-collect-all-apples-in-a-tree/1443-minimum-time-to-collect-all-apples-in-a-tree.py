class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        ans = 0
        visited = set()
        
        def dfs(root):
            nonlocal ans, visited
            apple = hasApple[root]
            
            if root in visited:
                return False
            
            visited.add(root)
            
            for child in graph[root]:
                childApple = dfs(child)
                apple = apple or childApple 
                
            if apple and root != 0:
                ans += 2
            return apple
                
        dfs(0)
        return ans
                
            
            
            
        