class Solution:
    def longestPrefix(self, s: str) -> str:
        lsp = [0] * len(s)
        n  = len(s)
        prev = 0
        i = 1
        
        while i < n:
            if s[prev] == s[i]:
                lsp[i] = prev + 1
                prev = lsp[i]
                i += 1
            else:
                if prev != 0:
                    prev = lsp[prev -1]
                else:
                    i += 1
        
        if lsp[-1] == 0:
            return ""
        else:
            return s[0:lsp[-1]]
        
        
        