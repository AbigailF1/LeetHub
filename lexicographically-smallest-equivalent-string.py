class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for i in range(len(s1)):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]

        def find(root):
            while root!= parent[root]:
                root = parent[root]
            return root

        def union(x,y):
            xf = find(x)
            yf = find(y)

            if xf < yf:
                parent[yf] = xf
            else:
                parent[xf] = yf

        for i in range(len(s1)):
            union(s1[i], s2[i])

        ans =""
        for lt in baseStr:
            if lt in parent:
                x = find(lt)
                ans += x
            else:
                ans += lt
        return ans