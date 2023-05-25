class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        leng = len(arr)
        for i in range(leng-2,-1,-1):
            # print(i)
            if arr[i] > arr[i+1]:
                # print(i, arr[i], arr[i+1])
                for j in range(leng-1,i,-1):
                    if arr[j] < arr[i] and (j == i-1 or arr[j] != arr[j-1]):
                        arr[i],arr[j] = arr[j],arr[i]
                        return arr
        return arr                
            
        