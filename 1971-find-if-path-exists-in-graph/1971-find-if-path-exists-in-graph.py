class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i:i for i in range(n)}
        rank = [1]* n
        
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
        
            if x_rep != y_rep:
                if rank[x_rep] >= rank[y_rep]:
                    rep[y_rep] = rep[x_rep]
                    rank[x_rep] += rank[y_rep]
                else:
                    rep[x_rep] = rep[y_rep]
                    rank[y_rep] += rank[x_rep]                               
                
        for i,j in edges:
            union(i,j)        
        return find(source) == find(destination)
        
                    
                    
                    
                    
                    
                    
               
                
                    
                    
                    
                
            
            
            
            
            
            
        