
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:cost[0], 1:cost[1]}
        cost.append(0)
        for i in range(2,len(cost)):
            memo[i] = min(memo[i-1], memo[i-2]) + cost[i]
        return memo[i]
                        
    
        