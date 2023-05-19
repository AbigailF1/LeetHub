class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        for i in range(26):
            rep[chr(97 + i)] = chr(97 + i)
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            rep[y_rep] = rep[x_rep]
            
        for i in equations:
            if i[1] == "=":
                union(i[0], i[3])
        for i in equations:
            if i[1] != "=":
                if find(i[0]) == find(i[3]):
                    return False
        # print(rep)
        return True