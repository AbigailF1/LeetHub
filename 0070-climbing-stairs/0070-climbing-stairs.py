memo ={}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        if n not in memo:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]
        
        