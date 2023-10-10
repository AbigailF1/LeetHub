class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        lsp = [0 ]*  len(needle)
        prev = 0
        i = 1
        
        while i < len(needle):
            if needle[prev] == needle[i]:
                lsp[i] = prev + 1
                prev = lsp[i]
                i += 1
            else:
                if prev != 0:
                    prev = lsp[prev -1]
                else:
                    i += 1
        
        l, r = 0,0  
        print(lsp)
        while(r < len(haystack)):
            
            if l == len(needle):
                return r - l
            if l == 0 and haystack[r] != needle[l]:
                r += 1
            elif haystack[r] == needle[l]:
                l+= 1
                r+= 1
            else:
                l = lsp[l-1]
        if l == len(needle):
                return r - l
            
        return -1
            
            
            
        