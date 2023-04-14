"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict(int)
        for i in range(len(employees)):
            dic[employees[i].id] = i
        count = 0
        def dfs(id, visited):
            nonlocal count 
            if id not in visited:
                visited.add(id)
            for i in employees[dic[id]].subordinates:
                if i not in visited:
                    dfs(i, visited)
            count += employees[dic[id]].importance
        dfs(id, set())         
        return count
    
                
                
            
        