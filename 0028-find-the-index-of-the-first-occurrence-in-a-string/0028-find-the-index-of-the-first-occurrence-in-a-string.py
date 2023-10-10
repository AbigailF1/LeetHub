class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)  > len(haystack):
            return -1
       
        n = len(needle) - 1
        summ = 0
        for letter in needle:
            summ += (ord(letter) - 96) * (26 ** n)
            n -= 1
            
        val = 0 
        l,r = 0, 0
        n = len(needle) - 1
        
        for letter in haystack:
            if (n < 0):
                break
            
            val += (ord(haystack[r]) - 96) * (26 ** (n)) 
            r += 1
            n -= 1
        
       
        # print(r, l,  haystack[l:r+1])
        n = len(needle) - 1
        r = n + 1
        
        while(r < len(haystack)):
            # print(val , summ, haystack[l:r+1])
            if val == summ:
                return l
            
            val -= (26 ** n )* ((ord(haystack[l]) - 96))
            val *= 26 
            val += (ord(haystack[r]) - 96)
                    
            l += 1
            r += 1
           
        if val == summ:
            return l
        
        return -1
            
            
            
            
        