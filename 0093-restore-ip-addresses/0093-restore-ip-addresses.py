class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        res = []
        
        def backtrack(num):
            nonlocal ans 
            nonlocal res
            if not num:
                if len(ans) == 4 :
                    res.append(".".join(list(map(str,ans))))
                if len(ans) > 4:
                    return
             
            for i in range(1, len(num) +1 ):
                if len(str(int(num[:i]))) == i and (int(num[:i]) < 256):
                    ans.append(int(num[:i]))
                    backtrack(num[i:])
                    ans.pop()
        backtrack(s)
        return res
        
        
            