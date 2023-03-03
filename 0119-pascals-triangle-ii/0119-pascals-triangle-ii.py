class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def recc(rowIndex):
            if rowIndex == 0:
                return [1]
            elif rowIndex == 1:
                return [1,1] 
            else:
                arr = recc(rowIndex-1)
                new_arr = [1]
                for i in range(1, len(arr)):
                    new_arr. append(arr[i] + arr[i-1])
                return new_arr + [1]
        return recc(rowIndex)