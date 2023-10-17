class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        
        if target % 2 != 0:
            return False
        
        target //= 2
        
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        
        for num in nums:
            for j in range(target, num -1, -1):
                dp[j] = dp[j] or dp[j-num]
            
            if dp[target]:
                return True
        return False
                

        
            
            
        
        
        
        
        