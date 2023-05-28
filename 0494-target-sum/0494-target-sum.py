class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backtrack(i, total):
            if i == len(nums):
                return 0 if total!= target else 1
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            
            return memo[(i, total)]
        
        return backtrack(0,0)