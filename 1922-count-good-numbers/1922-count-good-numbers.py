class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def multiply(a, b, m):
            return ((a % m) * (b % m)) % m

        def binary_exponentiation( base, exponent, mod):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result = multiply(base, result, mod)
                base = multiply(base, base, mod) 
                exponent >>= 1
            return result
        
        if n % 2 == 0:
            return binary_exponentiation( 5, n//2, 10**9 + 7 ) * binary_exponentiation( 4, n//2, 10**9 + 7 )% (10**9 + 7)
        else:
            if n == 1:
                return binary_exponentiation( 5, (n//2 + 1), 10**9 + 7 ) 
            else:
                return binary_exponentiation( 5, (n//2 + 1), 10**9 + 7 )  * binary_exponentiation( 4, n//2, 10**9 + 7 )% (10**9 + 7)