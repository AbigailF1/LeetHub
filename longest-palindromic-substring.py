class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for i in range(len(s))]
        max_, word = float("-inf"), ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                    dp[j][i] = 1
                    max_, word = 1, s[i]
                    
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                dp[i+1][i] = 1
                max_, word = 2, s[i:i+2]
                
        
        x = 2
        while x < len(s):
            for i in range(len(s)):
                j = i + x
                if j >= len(s):
                    break
                elif s[i] == s[j]:
                    if dp[i+1][j-1]:
                        dp[i][j] = 1
                        if (j - i + 1) > max_:
                            max_ , word = j - i + 1, s[i:j+1]
            x += 1
        # print(dp)     
        return word