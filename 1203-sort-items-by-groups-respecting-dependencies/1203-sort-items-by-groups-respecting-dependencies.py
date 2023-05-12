class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def sort_group(indx):
            group_order2 = defaultdict(int)
            dic2 = defaultdict(list)
            for i in (group_list[indx]):
                for j in group_dep[i]:
                    if group[i] == group[j]:
                        dic2[i].append(j)
                        group_order2[j] += 1
            queue = deque()
            for i in(group_list[indx]):
                if group_order2[i] == 0:
                    queue.append(i)
            arr = []
            while queue:
                x = queue.popleft()
                ans.append(x)
                for i in dic2[x]:
                    group_order2[i]-=1
                    if group_order2[i] == 0:
                        queue.append(i)
            return arr
                    
            
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m+=1
                
        dic = defaultdict(list)
        dep = [0]*m
        group_dep = defaultdict(list)
        group_list = defaultdict(list)
        
        for i in range(n): 
            group_list[group[i]].append(i)
            
        for i in range(len(beforeItems)):
            temp = beforeItems[i]
            for j in temp:
                if group[j]!= group[i]:
                    dic[group[j]].append(group[i])
                    dep[group[i]] += 1
                else:
                    group_dep[j].append(i)
      
        queue = deque()
        for i in range(len(dep)):
            if dep[i] == 0:
                queue.append(i)        
        group_order = []
        while queue:
            x = queue.popleft()
            group_order.append(x)
            for i in dic[x]:
                dep[i] -=1
                if dep[i] == 0:
                    queue.append(i)
        ans = []
        for i in group_order:
            ans.extend(sort_group(i))
    
        if len(ans)!= n:
            return[] 
               
        return ans
        