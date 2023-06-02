class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set([str(x) for x in range(1,27)])
        memo = [0] * (len(s) + 1)
        memo[-1] = 1
        for i in range(len(s) -1, -1,-1):
            if s[i] != '0':
                memo[i] += memo[i+1]
            if i + 1 < len(s) and s[i:i+2] in valid:
                memo[i] += memo[i+2]     
        return memo[0]
        
            
                
            
        