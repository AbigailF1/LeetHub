class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        rep = {i:i for i in range(n)}
        rank = [1]*(n)
            
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
        
        dic = defaultdict(set)
        for i in range(len(accounts)):
            dic[(i, accounts[i][0])] = set(accounts[i][1:])
            
        for i in dic:
            for j in dic:
                if i[0] != j[0] and i[1] == j[1]:
                    for x in dic[i]:
                        if x in dic[j]:
                            union(i[0],j[0])
        
        for i in range(n):
            repp = find(i)
            dic[(repp, accounts[repp][0])].update(dic[(i,accounts[i][0])])
        ans = []
        for i in range(n):
            if rep[i] == i:
                temp = [accounts[i][0]] + list(sorted(list(dic[(i,accounts[i][0])])))
                ans.append(temp)
        return ans
        
                               