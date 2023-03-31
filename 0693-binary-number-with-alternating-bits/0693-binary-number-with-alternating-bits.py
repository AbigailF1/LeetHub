class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        
        for i in range(1, int(math.log(n, 2))+1):  
            if  n & (1 << i):
                cur = 1
            else:
                cur = 0
            
            if cur == prev:
                return False 
            prev = cur 
            
        return True 
                