class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}
        n = len(stones)
        
        @cache
        def dp(i, target):
            
            if i >= n:
                 return target if target >= 0 else float('inf')
            
            x = min(dp(i+1, target + stones[i]),dp(i+1, target - stones[i]))             
            return x
        
        return dp(0,0)
                         
            
            