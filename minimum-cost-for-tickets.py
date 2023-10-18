class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = max(days)
        dp = [0] * (n + 1)
        
        set_days = set(days)
        for i in range(n + 1):
            if i in set_days:
                dp[i] = min(dp[max(i - 1,0)] + costs[0], dp[max(i - 7,0)]+ costs[1], dp[max(i -30,0)] + costs[2])
            else:
                dp[i] = dp[max(i - 1, 0)]

        return dp[-1]
            
        


#         @cache
#         def dp(i):
            
#             return min(dp(min(i -1,0) + costs[0]), dp(min(i - 7,0)+ costs[1]), dp(min(i -30,0) + costs[2]))
#         return dp(0)