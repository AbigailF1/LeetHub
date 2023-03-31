class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [i for i in range(1, n+1)]
        i = 0
        while len(array) > 1:
            i = i - 1 + k
            if i >= len(array):
                i = i % len(array)
            array.pop(i)
        return array[0]
                
            
