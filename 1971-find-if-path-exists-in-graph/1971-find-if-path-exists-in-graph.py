class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = defaultdict(list)
        for edge in edges:
            path[edge[0]].append(edge[1])
            path[edge[1]].append(edge[0])
            
        visited = set() 
        def check_path(source, visited):
            if source in visited:
                return
            visited.add(source)
    
            if source == destination:
                return True
            for num in path[source]:
                find = check_path(num, visited)

                if find :
                    return True
            return False
        return check_path(source, visited)
        
                    
                    
                    
                    
                    
                    
               
                
                    
                    
                    
                
            
            
            
            
            
            
        