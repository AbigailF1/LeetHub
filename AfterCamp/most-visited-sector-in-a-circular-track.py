class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        dic = defaultdict(int)
        dic[rounds[0]] += 1
        for i in range(1,len(rounds)):
            end = rounds[i]
            start = rounds[i -1]
            while start != end:
                if start >= n:
                    start = 1
                else:
                    start += 1
                dic[start] += 1   
        numm = max(dic.values())
        ans = []
        for key, val in dic.items():
            if val == numm:
                ans.append(key)
        return sorted(ans)