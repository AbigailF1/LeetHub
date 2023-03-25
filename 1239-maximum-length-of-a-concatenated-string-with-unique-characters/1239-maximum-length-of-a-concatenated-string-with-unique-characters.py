class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maximum = -inf
        
        def backtrack(indx, ans):
            nonlocal maximum 
            maximum = max(maximum, len(ans))
            
            if indx == len(arr):
                return 
                          
            for i in range(indx,len(arr)):
                if len(arr[i]) + len(ans) == len(set(list(arr[i]) + list(ans))):
                    new_ans = ans.copy()
                          
                    for j in arr[i]:
                         ans.add(j)
                          
                    backtrack(i+1, ans)
                    ans = new_ans
        backtrack(0, set())
        return maximum 
            
                        
                          
                
        