class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) -1
        m = len(text2) - 1 
        memo = {}
        def longest(i,j):
            if i < 0 or j < 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + longest(i-1,j-1)
            else:
                memo[(i,j)] = max(longest(i,j-1), longest(i -1 ,j))
            return memo[(i,j)]
        return longest(n,m)