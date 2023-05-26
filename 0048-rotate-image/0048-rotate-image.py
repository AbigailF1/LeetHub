class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        visited = set()
        for i in range(n):
            for j in range(n):
                temp = matrix[i][j]
                if (i,j) not in visited and (j,i) not in visited:
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    visited.add((i,j))
                    visited.add((j,i))
                # print(i,j,temp)
        for i in range(n):
            matrix[i].reverse()
        return matrix