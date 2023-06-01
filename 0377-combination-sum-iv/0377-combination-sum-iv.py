class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        for summ in range(1, target + 1):
            for n in nums:
                if summ - n >= 0:
                    memo[summ] += memo[summ - n]
        # print(memo)
        return memo[target]