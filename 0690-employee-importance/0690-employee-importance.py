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
        s = []
        count = 0
        dic = defaultdict(list)
        for emp in employees:
            dic[emp.id] = [emp.subordinates, emp.importance]
            #print(dic)
        s.append(id)
        while s:
            #print(s)
            top = s.pop()
            count += dic[top][1]
            s+= dic[top][0]
        return count 
                
                
            
        