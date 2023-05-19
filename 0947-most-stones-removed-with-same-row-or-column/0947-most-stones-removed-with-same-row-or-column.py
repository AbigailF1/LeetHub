class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {i:i for i in range(len(stones))}
        rank = [1] * len(stones)
        def find(x):
            if x == rep[x]:
                return x
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
        for i in range(len(stones)):
            for j in range(i, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        count = 0
        for i in range(len(stones)):
            if rep[i] != i:
                count += 1
        return count
        