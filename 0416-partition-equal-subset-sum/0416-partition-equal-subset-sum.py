class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        
        if target % 2 != 0:
            return False
        
        target //= 2
        
        @cache
        def dp(i, sum_):
            if sum_ == target:
                return True
            
            if i >= len(nums):
                return False
            
            if sum_ > target:
                return False
            
            return dp(i + 1, sum_+ nums[i]) or dp(i + 1 , sum_)
        
        return dp(0, 0)
            
            
        
        
        
        
        