class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o={'(':')', '{':'}', '[':']' }
        for i in range(len(s)):
            if s[i] in o:
                stack.append(s[i])
            else:
                if stack and s[i]==o[stack[-1]]:# {([])
                    stack.pop()
                else:
                    return False  
        if not stack:
            return True 
        else:
            return False