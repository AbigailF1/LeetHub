class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy = [0]*(n+2)
        sell = [0] * (n+2)
        
        
        for i in range(n-1,-1,-1):
            for cooldown in range(2):
                if cooldown:
                    buy[i] = (max(sell[i+1] - prices[i], buy[i+1]))
                else:
                    sell[i] = (max(buy[i+2]+ prices[i], sell[i+1]))
        return buy[0]
            
        