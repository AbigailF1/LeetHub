class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(sum_):
            
            if sum_ > amount:
                return float('inf')
            
            if sum_ == amount:
                return 0
            
            min_ = float('inf')
            for coin in coins:
                min_ = min(min_, dp(sum_ + coin) + 1)
                
            return min_
    
        ans = dp(0)
        return -1 if ans == float('inf') else ans
        