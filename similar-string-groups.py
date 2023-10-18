class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {}
        for i in range(len(strs)):
            rep[strs[i]] = strs[i]
        rank = {x: 1 for x in strs}
                  
        def find(x):
            while x!= rep[x]:
                x = rep[x]
            return x

        def union(x, y):
            xf = find(x)
            yf = find(y)

            if xf!= yf:
                if rank[xf] > rank[yf]:
                    rep[yf] = xf
                    rank[xf] += 1
                else:
                    rep[xf] = yf
                    rank[yf] += 1  
       
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                count = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k] :
                        count += 1
                if count < 3:
                    union(strs[i], strs[j])
        ans = defaultdict(int)
        for i in range(len(strs)):
            ans[find(strs[i])] += 1
        print(ans)
        return len(ans)