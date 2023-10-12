class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        letter = {chr(i+97):i+1 for i in range(26)}
        
        arr = [1]
        
        for i in range(k):
            val = arr[-1] * power 
            arr.append(val)
       
            
        hashfind = 0
        for i in range(k):
            hashfind += (arr[i] * (letter[s[i]]))
            
        l = 0
        r = k
        
        while r < len(s):
            if hashfind % modulo == hashValue:
                return s[l:r]
            
            hashfind -= letter[s[l]]
            hashfind //= power
            hashfind += letter[s[r]] * arr[k-1]
            
            r += 1
            l += 1
            
        if hashfind%modulo == hashValue:
            return s[l:r]
    
# class Solution:
# this solution excceeds the time limit so we can precalculate the powers to k
#     def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
#         val = 0 
        
#         for i in range(k):
#             val += (ord(s[i]) - 96) * (power ** (i)) 
            
#         l,r = 0, k
        
#         while (r < len(s)):
#             if  hashValue == val% modulo:
#                 return s[l:r]
            
#             val -= ((ord(s[l]) - 96))
#             val //= power 
#             val += ( (ord(s[r]) - 96) * (power ** (k-1)) )
            

#             l += 1
#             r += 1
        
#         if  hashValue == val%modulo:
#             return s[l:r]
        
            
            