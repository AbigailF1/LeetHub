class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            ans = [[1]] 
        else:
            ans = [[1], [1,1]]
        for i in range(1,numRows-1):
            res =[1]
            for j in range(1,len(ans[i])):
                res.append(ans[i][j] + ans[i][j-1])
            res.append(1)
            ans.append(res)
            
        return ans
                
                
                
        