class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans =[]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".": 
                    ans += [(i, num), (num,j), (i//3, j//3, num)]
        return len(ans) == len(set(ans))