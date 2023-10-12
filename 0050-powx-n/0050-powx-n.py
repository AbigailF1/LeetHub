class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        def calculate(x,n):
            nonlocal result
            while n > 0:
                if n & 1:
                    result *= x

                x *= x
                n>>=1
                
            
        if n > 0:
            calculate(x,n)
            return result
        elif n <  0:
            calculate (x, (-n))
            return 1/result
        return result
            