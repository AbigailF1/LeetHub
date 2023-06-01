class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = [prices[0]]
        sell = 0
        
        for i in range(len(prices)):
            sell = max(sell, prices[i] - buy[-1] - fee)
            buy.append(min(buy[-1], prices[i] - sell))
        return sell
        