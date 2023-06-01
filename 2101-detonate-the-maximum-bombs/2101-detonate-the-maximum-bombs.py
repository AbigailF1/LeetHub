class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                distance = sqrt(pow((bombs[i][0]-bombs[j][0]),2) + pow((bombs[i][1]-bombs[j][1]),2))

                if bombs[i][2] >= distance:
                    graph[i].append(j)
                if bombs[j][2] >= distance:
                    graph[j].append(i)
        
        maxx = 0
        visited = set()
        
        def dfs(node):
            
            count = 0
            visited.add(node)
            for ele in graph[node]:
                if ele not in visited:
                    count += dfs(ele)
            return count + 1
        
        for i in range(len(bombs)):
            maxx = max(maxx, dfs(i))
            visited = set()
        return maxx
                
        