class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        set_ = set(arr)
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                
                x, y = arr[j], arr[j] + arr[i]
                len_ = 2
                
                while y in set_:
                    x, y = y, y + x
                    len_ += 1
                
                ans = max(ans, len_)
        
        if ans > 2 :
            return ans 
        else:
            return 0
            
        