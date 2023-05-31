class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = [inf]
        sell = [-inf]
        
        for i in range(len(prices)):
            if buy[-1] != inf:
                sell.append(max(sell[-1], prices[i] - buy[-1] - fee))
            if sell[-1]!= -inf:
                buy.append(min(buy[-1], prices[i] - sell[-1]))
            else:
                buy[-1] = prices[i]
                sell[-1] = 0
        # print(buy)
        # print(sell)
        return max(sell)
        