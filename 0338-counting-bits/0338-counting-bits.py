class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            no_ones = 0
            element = i 
            while element != 0:
                if element % 2 != 0:
                    no_ones += 1
                    element = element // 2
                else:
                    element = element // 2
            arr.append(no_ones)
        return arr
                    
                     

             
            
                    

            
            