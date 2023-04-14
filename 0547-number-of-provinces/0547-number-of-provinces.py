class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    dic[i].append(j)
        count = 0
        def dfs(province):
            nonlocal count 
            if province not in visited:
                visited.add(province)
                for i in dic[province]:
                    dfs(i)
            return 
        visited = set()
        for i in dic:
            if i not in visited:
                dfs(i)
                count += 1
        return count
        