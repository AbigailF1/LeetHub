class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat[0]) * len(mat) != r*c:
            return mat
        
        new_matrix = [[0]*c for i in range(r)]
        index = 0
        
        for i in range(len(mat)):  
            for j in range(len(mat[0])):
                row = index//c
                column = index % c
                new_matrix[row][column] = mat[i][j]
                index += 1
        return new_matrix
        