class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        l, r = 0, 0
        len_t = len(dic)
        len_s = len(s)
        ans = len_s + 1
        
        if len(t) > len(s):
            return ""
       
        for i in range(len_s):
            
            if s[i] in dic:
                dic[s[i]] -= 1
                
                if dic[s[i]] == 0:
                    len_t -=1
                
                while len_t == 0:
                    
                    if ans > i - l + 1:
                        ans = i - l + 1
                        r = l
                    
                    if s[l] in dic:
                        dic[s[l]] += 1
                        
                        if dic[s[l]]>0:
                            len_t += 1
                    l += 1
        if ans > len(s):
            return ""
        
        return s[r: r + ans]
 
                    
                
                