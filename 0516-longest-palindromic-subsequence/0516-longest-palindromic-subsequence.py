class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s) -1
        s2 = s[::-1]
        m = len(s2) - 1 
        memo = {}
        # dp function 
        def longest(i,j):
            if i < 0 or j < 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == s2[j]:
                memo[(i,j)] = 1 + longest(i-1,j-1)
            else:
                memo[(i,j)] = max(longest(i,j-1), longest(i -1 ,j))
            return memo[(i,j)]
        return longest(n,m)
        