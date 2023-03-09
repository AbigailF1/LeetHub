class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 
        elif  n == 1:
            return x 
        if n > 0:
            number = self.myPow(x,n//2)
            if n % 2 == 0:
                return number * number
            return x* number * number   
        return 1/(self.myPow(x,abs(n)))
        