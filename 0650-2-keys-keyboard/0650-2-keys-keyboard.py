class Solution:
    def minSteps(self, n: int) -> int:
        prime_factors = []
        d = 2
        
        while d * d <= n:
            
            while n % d == 0:
                
                prime_factors.append(d)
                n //= d
            d += 1
        if n > 1:
            prime_factors.append(n)
        
        count = 0
        for i in prime_factors:
            count += i
            
        return count
        
        