class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def dp(i, state):
            if i == len(nums):
                return 0
                       
            if state:
                return max(nums[i] + dp(i+1, 1 - state), dp(i+1, state))
            else:
                return max(-nums[i] + dp(i+1, 1 - state), dp(i+1, state))
            
        
        return dp(0, 1)