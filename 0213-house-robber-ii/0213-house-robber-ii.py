class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(n, end):
            
            if n < end:
                return 0
            
            if n == end:
                return nums[end]
            
            if  n not in memo:
                memo[n] = max(dp(n-1, end), dp(n-2, end) + nums[n])   
            return memo[n]
        y = dp(len(nums) -1, 1)
        memo = {}
        z = dp(len(nums) -2, 0)
        
        if len(nums) > 1:
            x = max(z,y)
            return x    
        else:
            return (nums[0])
        