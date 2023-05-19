class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
            
        rep = {i:i for i in range(len(points))}
        rank = [1] * len(points)
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            if x_rep == y_rep:
                return True

            if rank[x_rep] >= rank[y_rep]:
                rep[y_rep] = rep[x_rep]
                rank[x_rep] += rank[y_rep]
            else:
                rep[x_rep] = rep[y_rep]
                rank[y_rep] += rank[x_rep]
            return False
            
        total = 0
        ans = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i!= j:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    ans.append([dist, i, j])
        ans.sort()
        for dist, i, j in ans:
            if not union(i,j):
                total += dist
          
        return total