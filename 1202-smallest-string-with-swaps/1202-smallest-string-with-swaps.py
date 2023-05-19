class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {}
        rank = [1]* (len(s))
        for i in range(len(s)):
            rep[i] = i
            
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
                    
        for i, j in pairs:
            union(i,j)
            
        ans = list(s)
        res = defaultdict(list)
        for i in range(len(s)):
            res[find(i)].append(i)
        for val in res.values():
            order = []
            for i in val:
                order.append(s[i])
            order.sort()
            for i in range(len(val)):
                ans[val[i]] = order[i]
      
        return "".join(ans)