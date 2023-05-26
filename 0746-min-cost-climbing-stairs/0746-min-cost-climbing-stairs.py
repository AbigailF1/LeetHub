
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost.append(0)
        def fib(i):
            if i == 0 or i== 1:
                memo[i] = cost[i]
            if i not in memo:
                if fib(i-1) > fib(i -2):
                    memo[i] = fib(i-2) + cost[i]
                else:
                    memo[i] = fib(i-1) + cost[i]
            return memo[i]
        return fib(len(cost) -1)
        