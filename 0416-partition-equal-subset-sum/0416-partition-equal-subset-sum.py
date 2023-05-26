class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, k):
            if i >= len(nums) or k <=0:
                return k == 0
            state = (i, k)
            if state not in memo:
                memo[state] = dp(i+1, k) or dp(i+1, k - nums[i])
            return memo[state]
        
        memo = defaultdict(int)
        return sum(nums) % 2 == 0 and dp(0, sum(nums)//2)
        
        