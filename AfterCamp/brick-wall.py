class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        dic = defaultdict(int)
        dic[sum(wall[0])] = 0

        for i in range(n):
            pre_sum = 0
            for j in range(len(wall[i]) -1):
                pre_sum += wall[i][j]
                dic[pre_sum] += 1
        
        return n - max(dic.values()) 
                


        