class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(current_num, path,k):
            if current_num > n+1:
                return 
            if len(path) == k:
                ans.append(path[::])
                return 
            path.append(current_num)
            backtrack(current_num + 1, path,k)
            path.pop()
            backtrack(current_num + 1, path,k)
        backtrack(1, [], k)
        return ans 
                
                