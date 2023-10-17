class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(sum_, indx):
            # print(sum_, indx)
            if amount == sum_:
                return 1
            
            if indx >= len(coins) or sum_ > amount:
                return 0
            
            return dp(sum_ + coins[indx], indx) + dp(sum_ , indx + 1)
    
        return dp(0,0)
        
        
        