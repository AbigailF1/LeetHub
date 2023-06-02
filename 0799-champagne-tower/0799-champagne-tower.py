class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[0] * (query_row + 2) for i in range(query_row + 2) ]
        memo[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(0,i+1):
                if memo[i][j] > 1:
                    memo[i +1][j] += (memo[i][j] - 1)/2
                    memo[i +1][j + 1] +=(memo[i][j] - 1)/2
                    memo[i][j] = 1
        
        return memo[query_row][query_glass]
            
        