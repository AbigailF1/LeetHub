class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        def backtrack(num):
            if not num:
                if len(ans) > 2:
                    return True 
                return False
            
            for i in range(1, len(num) +1 ):
                if len(str(int(num[:i]))) == i and  ( len(ans) < 2 or int(num[:i]) == int(ans[-2]) + int(ans[-1])):
                    ans.append(int(num[:i]))
                    if backtrack(num[i:]):
                        return True
                    ans.pop()
            return False 
        return backtrack(num)
        
        