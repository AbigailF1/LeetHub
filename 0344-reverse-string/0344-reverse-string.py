class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                x = s[r]
                s[r] = s[l]
                s[l] = x
                l+=1
                r-=1
            else:
                l+=1
                r-=1
        return s 
        
        """
        Do not return anything, modify s in-place instead.
        """
        