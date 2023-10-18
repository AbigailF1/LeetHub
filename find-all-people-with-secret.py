class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        rep = {}
        for i in range(n):
            if i == firstPerson:
                rep[i] = 0
            else:
                rep[i] = i
        print(rep)

        meetings.sort(key = lambda item:(item[2], item[0]))
        meet_time = defaultdict(list)
        meet_time[0].append([0,firstPerson])
        for x, y, z in meetings:
            meet_time[z].append([x,y])


        rank = [1] *(n)
           
        def find(x):
            while x!= rep[x]:
                x = rep[x]
            return x

        def union(x, y):
            xf = find(x)
            yf = find(y)

            if xf!= yf:
                
                if xf == 0:
                    rep[yf] = xf
                elif yf == 0:
                    rep[xf] = yf
                elif rank[xf] > rank[yf]:
                    rep[yf] = xf
                    rank[xf] += 1
                else:
                    rep[xf] =  yf
                    rank[yf] += 1 
           
        ans = set()
        for key, items in meet_time.items():
            for x, y in items:
                union(x,y)
            for x, y in items:
                if find(x) == find(0):
                    ans.add(x)
                    ans.add(y)
                else:
                    rep[x] = x
                    rep[y] = y
        return list(ans)