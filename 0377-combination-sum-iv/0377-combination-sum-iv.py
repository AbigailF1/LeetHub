class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        
        def dp(target):
            if target not in memo:
                if target == 0:
                    memo[0] = 1
                if target < 0:
                    return 0

                for n in nums:
                    memo[target] += dp(target - n)
            return memo[target]
        
        return dp(target)