class Solution:
    def fib(self, n: int) -> int:
        memo ={0:0, 1:1}
        def f(n):
            nonlocal memo
            if n == 0 or n == 1:
                return n
            if n not in memo:
                memo[n] = f(n-1) + f(n -2) 
            return memo[n]
        return f(n)
    
        
            
            
       
        
        