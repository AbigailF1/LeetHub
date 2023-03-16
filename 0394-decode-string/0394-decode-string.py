class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in s:
            
            if i == "]":
                ans = ""
                
                while stack[-1]!= "[":
                    ans = stack.pop() + ans 
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number 
                    
                ans *= int(number)
                stack.append(ans)
            else:
                stack.append(i)
        return "".join(stack)
        