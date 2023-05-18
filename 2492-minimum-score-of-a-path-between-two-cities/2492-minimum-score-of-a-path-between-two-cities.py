class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i:i for i in range(n + 1)}
        rank = [1]* (n+1)
        
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
        for i,j,path in roads:
            x = union(i,j)
        minn = inf
        for i,j,path in roads:
            if find(1) == find(i):
                minn = min(minn, path)
        return minn              