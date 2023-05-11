class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        dic = defaultdict(list)
        for i,j in edges:
            dic[i].append(j)
            dic[j].append(i)
            
         
        queue = deque()
        for i in range(len(dic)):
            if len(dic[i]) == 1:
                queue.append(i)
        nodes = n
        while nodes > 2:
            for i in range(len(queue)):
                x = queue.popleft()
                nodes -= 1
                
                parent = dic[x].pop()
                dic[parent].remove(x)
                
                if len(dic[parent])== 1:
                    queue.append(parent)
        return queue
            