class Solution:
    def fib(self, n: int) -> int:
        F=[0 for x in range(n+1)]
        F[0]=0
        if n>=1:
            F[1]=1
            for x in range(2,n+1):
                F[x]=F[x- 1] +F[x- 2]
        return F[-1]
                
            
            
       
        
        