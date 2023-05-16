class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerorow= set()
        zerocol = set()
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zerorow.add(r)
                    zerocol.add(c)
                    
        for r in range(row):
            for c in range(col):
                if r in zerorow or c in zerocol:
                    matrix[r][c] = 0
    
        