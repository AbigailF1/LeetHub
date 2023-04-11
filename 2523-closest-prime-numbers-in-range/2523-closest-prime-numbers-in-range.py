class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):                   
                    for i in range(p * p, num+1, p):
                        prime[i] = False               
                p += 1
            return prime
        
        primes = SieveOfEratosthenes(right)
        primes[1] = False
        ans = [-1,-1]
        prev = None
        minn = inf
        for i in range(left, right+1):
            if primes[i] == True:
                if prev != None and (minn > i - prev):
                    minn = i - prev
                    ans = [prev, i]
                    if minn <= 2:
                        return ans
                prev = i
        
        return ans