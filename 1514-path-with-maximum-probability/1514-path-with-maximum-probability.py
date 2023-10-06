class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        max_path = [0] * n
        max_path[start_node] = 1
        # print(max_path)
        
        for i in range(n-1):
            flag = 0
            for j in range(len(edges)):
                u, v =  edges[j]
                lenn = succProb[j]
                
                if max_path[u] * lenn >  max_path[v]:
                    max_path[v] = max_path[u] * lenn
                    flag = 1
                
                if max_path[v] * lenn >  max_path[u]:
                    max_path[u] = max_path[v] * lenn
                    flag = 1
                    
            if not flag:
                break
                    
                    
        return max_path[end_node]
                    
                
        
        