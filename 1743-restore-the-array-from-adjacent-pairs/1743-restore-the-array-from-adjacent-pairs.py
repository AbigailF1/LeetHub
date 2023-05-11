class Solution:
    def restoreArray(self, ap: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        # incoming = defaultdict(int)
        for i in range(len(ap)):
            dic[ap[i][0]].append(ap[i][1])
            dic[ap[i][1]].append(ap[i][0])
            # incoming[ap[i][1]] += 1
            # incoming[ap[i][0]] += 1
            
        ans = []
        visited = set()
        for i in dic:
            if len(dic[i]) == 1:
                ans.append(i)
                visited.add(i)
                break
        while len(ap) >= len(ans):
            x = ans[-1]
            for i in dic[x]:
                if i not in visited:
                    ans.append(i)
                    visited.add(i)
       
        return ans
        