class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(current_num, path):
            if current_num > n+1:
                return 
            if len(path) == k:
                ans.append(path[::])
            for i in range(current_num, n+1):   
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return ans 
                
                