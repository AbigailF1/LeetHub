class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set([str(x) for x in range(1,27)])
        memo = defaultdict(int)
        
        def dp(i):
            if i == len(s):
                return 1
            if i not in memo:
                take_1, take_2 = 0,0    
                if s[i] != '0': 
                    take_1 = dp(i+1)
                if i + 1 < len(s) and s[i:i+2] in valid:
                    take_2 = dp(i+2)
                memo[i] = take_1 + take_2 
            return memo[i]
            
        
        return dp(0)
        
            
                
            
        