class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
        for i in range(n -1, -1,-1):
            ans += mat[i][abs(n-i -1)]
            
        if n % 2 != 0:
            i = (n)//2
            ans -= mat[i][i]
        return ans
            