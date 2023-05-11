class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i,j in edges:
            dic[i].append(j)
            dic[j].append(i)
            
        max_height = [0]*n
        edge_count = [0]*n
        
        for i in range(len(dic)):
            edge_count[i] = len(dic[i])
            
        visited = set()  
        queue = deque()
        for i in range(len(dic)):
            if edge_count[i] == 1:
                queue.append(i)
                visited.add(i)
        left_edges = n-1
        while left_edges > 1 :
            x = queue.popleft()
            left_edges-=1
            for i in dic[x]:
                edge_count[i]-=1
                if i not in visited:
                    max_height[i] = max(max_height[i] ,max_height[x]+1)
                if edge_count[i] == 1:
                    queue.append(i)
                    visited.add(i)
        ans = []
        maxx = max(max_height)
        for i in range(len(max_height)):
            if maxx == max_height[i]:
                ans.append(i)
                    
        print(max_height)
        return ans