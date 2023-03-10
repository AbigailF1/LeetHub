class Solution:
    def splitString(self, s: str) -> bool:
        ans =[]
        t_f = False
        def backtrack(candidate):
            nonlocal t_f
            if not (candidate):
                if len(ans) > 1:
                    t_f = True 
                return 
            
            for j in range(1, len(candidate) + 1):
                val = int(candidate[:j])
                if len(ans) == 0 or int(ans[-1]) == val + 1:
                    ans.append(val)
                    backtrack(candidate[j:])
            if ans:
                ans.pop()
            return 
                
        backtrack(s)
        return t_f
        