class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in dic:
                    if dic[i-j] != matrix[i][j]:
                        return False 
                else:
                    dic[i-j] = matrix[i][j]
        return True
                
        