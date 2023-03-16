class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 
        length = 2**(n-1)
        mid = length / 2
        if mid >= k:
            x = self.kthGrammar(n-1, k)
            return x
        elif mid < k:
            x = self.kthGrammar(n-1, k -mid)
            if x == 0:
                return 1
            return 0

            