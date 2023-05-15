class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for i, j in dislikes:
            dic[i].append(j)
            dic[j].append(i)
        visited = set()
        def bfs(i):
            color = {i:0}

            queue = deque()
            visited.add(i)
            queue.append(i)
            while queue:
                x = queue.popleft()
                n_color = 1 - color[x]
                for i in dic[x]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
                        color[i] = n_color
                    elif color[i] != n_color:
                        return False
            return True
        for i in range(1, n + 1):
            if i not in visited:
                if not bfs(i):
                    return False
        
        return True
            