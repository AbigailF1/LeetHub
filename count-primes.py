class Solution:
    def countPrimes(self, n: int) -> int:
        def SieveOfEratosthenes(num):
            count = 0
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):

                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            for p in range(2, num+1):
                if prime[p]:
                    count += 1
            return count
        return SieveOfEratosthenes(n - 1)