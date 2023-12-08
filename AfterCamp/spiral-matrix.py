class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row = len(matrix)
        col = len(matrix[0])
        
        top, down = 0, row -1
        left, right = 0, col -1
        drc = 0
        while top <= down and left <= right:
            if drc==0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
                drc = 1
            elif drc == 1:
                for i in range(top, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
                drc = 2
            elif drc == 2:
                for i in range(right,left -1,-1):
                    ans.append(matrix[down][i])
                down -= 1
                drc = 3
            elif drc == 3:
                for i in range(down, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
                drc = 0
        return ans
                
            

            
        