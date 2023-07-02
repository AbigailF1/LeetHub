class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row < 3 or col<3:
            return 0
        def check(a,b,c,d,e,f,g,h,i):
            return(sorted([a,b,c,d,e,f,g,h,i]) == [1, 2, 3, 4, 5, 6, 7, 8, 9] and (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))
        ans = 0
        for r in range(row - 2):
            for c in range(col - 2):
                
                if check(grid[r][c],grid[r][c+1],grid[r][c+2],grid[r+1][c],grid[r+1][c+1],grid[r + 1][c+2],grid[r + 2][c],grid[r+2][c+1],grid[r+2][c+2]):
                    ans += 1
        return ans
                    

            
        