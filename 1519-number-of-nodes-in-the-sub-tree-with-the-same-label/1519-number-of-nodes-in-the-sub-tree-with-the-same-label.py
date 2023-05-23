class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(root, val):
            nonlocal arr
            count = [0] * 26
            count[ord(labels[root]) - 97] = 1
            
            for neighbour in graph[root]:
                if neighbour == val:
                    continue
                childcount = dfs(neighbour, root)
                for i in range(26):
                    count[i] += childcount[i]
            arr[root] = count[ord(labels[root]) - 97]
            return count
        arr = [1]*n
        dfs(0, -1)
        return arr
       
        
            
        