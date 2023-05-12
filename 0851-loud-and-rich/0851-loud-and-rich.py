class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic = defaultdict(list)
        indegree = [0] * len(quiet)
        
        for rich, poor in richer:
            dic[rich].append(poor)
            indegree[poor]+=1

        queue = deque()
        for i in range(len(quiet)):
            if indegree[i]==0:
                queue.append(i)
        
        ans = [i for i in range(len(quiet))]
        while queue:
            x = queue.popleft()
            sil = quiet[x]
            
            for i in dic[x]:
                indegree[i] -=1
                if indegree[i] == 0:
                    queue.append(i)
                if sil < quiet[i]:
                    ans[i] = ans[x]
                    quiet[i] = sil
        return ans
                