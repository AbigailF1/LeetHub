class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False 
        i = 0
        j = len(arr) - 1
        leng = len(arr)
        while i + 1 < leng and arr[i] < arr[i+1]:
            i+=1
        while j > 0 and arr[j-1] > arr[j]:
            j -=1
        return 0 < i == j < leng - 1
        
        