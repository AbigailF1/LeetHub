class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {0:nums[0]}
        for i in range(1,n):
            if i == 1:
                memo[i] = max(memo[i-1], nums[i])
            else:
                memo[i] = max(memo[i-1], memo[i-2]+ nums[i])
        return memo[n-1]
        
            
        