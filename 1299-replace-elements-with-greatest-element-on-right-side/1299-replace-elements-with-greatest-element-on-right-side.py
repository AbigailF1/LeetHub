class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > maxx:
                arr[i], maxx = maxx , arr[i]
            else:
                arr[i] = maxx
        return arr

                
        