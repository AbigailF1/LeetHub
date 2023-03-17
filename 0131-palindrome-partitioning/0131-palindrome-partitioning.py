class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            s  = "".join(filter(str.isalnum, s.lower()))
            l , r = 0, len(s)-1
            while l < r:
                if s[l]!= s[r]:
                    return False 
                l += 1
                r -= 1
            return True 
        ans = []
        def backtrack(s, i,res):
            if i >= len(s):
                ans.append(res.copy())
                return 
            for j in range(i+1, len(s) + 1 ):
                if isPalindrome(s[i:j]):
                    res.append(s[i:j])
                    backtrack(s, j, res)
                    res.pop()
        
        backtrack(s, 0 , [])
        return ans         
            