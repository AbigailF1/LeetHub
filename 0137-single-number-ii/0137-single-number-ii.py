class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = [0] * 32 
        _num = 0
        for i in nums:
            if i < 0:
                _num += 1
            for j in range(32):
                if abs(i) & (1 << j ) != 0:
                    arr[j]+= 1
        
        element = 0
        for k in range(32):
            if arr[k] % 3 != 0:
                element += pow(2, k)
        if _num % 3 != 0:
            element = -element
        return element
                
            
        
                

            