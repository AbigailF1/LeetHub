class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        dp = {}
        
        def dfs(i, state):
            if i == len(nums):
                return 0
            if (i,state) in dp:
                return dp[(i,state)]
            
            if state:
                summ = nums[i]
            else:
                summ = nums[i] * (-1)
            
            dp[(i,state)] = max(summ + dfs(i+1, 1 - state), dfs(i+1, state))
            
            return dp[(i,state)]
        
        return dfs(0, 1)