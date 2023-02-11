class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        op=['+', '-', '*', '/']
        for i in tokens:
            if i not in op:
                arr.append(int(i)) # you are doing good keep it up!![10,6,9,3]
            else:
                if i=="+":
                    x=arr.pop(-2)+arr.pop(-1)
                    arr.append(x)
                elif i=="-":
                    x=arr.pop(-2)-arr.pop(-1)
                    arr.append(x)
                elif i=="*":
                    x=arr.pop(-2)*arr.pop(-1) 
                    arr.append(x)        
                elif i=="/":
                    b = arr.pop()
                    a = arr.pop()
                    x= a//b if a/b > 0 else -(-a//b)
                    arr.append(x)
        return(arr[0])
        
        
        