class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
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
        
        b = int("".join(str(i) for i in b ))
        # print(b)
        return binary_exponentiation(a, b, 1337)
        