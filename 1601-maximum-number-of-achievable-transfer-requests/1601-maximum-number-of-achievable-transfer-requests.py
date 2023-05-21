class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        count = 0
        
        def backtrack(i,arr):
            nonlocal count
            
            if i == len(requests):
                arr2 = [0]*n
                for i in range(len(requests)):
                    if arr[i] == 1:
                        arr2[requests[i][0]] -= 1
                        arr2[requests[i][1]] += 1
                
                if arr2.count(0) == len(arr2): 
                    count = max(count,sum(arr))
                    
                return
            arr2 = arr.copy()
            backtrack(i+1,arr)
            arr2[i] = 1
            backtrack(i+1,arr2)
            return 
        backtrack(0,[0]*len(requests))
        return count
        