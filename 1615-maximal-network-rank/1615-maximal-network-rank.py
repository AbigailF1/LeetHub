class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        dic = defaultdict(int)
        for i, j in roads:
            graph[i]+=1
            graph[j]+=1
        for i in range(n):
            for j in range(i+1, n):
                if [i,j] in roads or [j,i] in roads:
                    dic[(i, j)] = graph[i] + graph[j] - 1
                else:
                    dic[(i, j)] = graph[i] + graph[j]
        return max(dic.values())
        
                
    