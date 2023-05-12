class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(right):
            left = 0
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
                left += 1
        
        ans = []

        
        for i in range(len(arr) -1, -1, -1):
            maxx = i
            for j in range(i, -1,  -1):
                if arr[j] > arr[maxx]:
                    maxx = j
            if maxx != i:
                flip(maxx)
                ans.append(maxx + 1)
                flip(i)
                ans.append(i + 1)
        return ans
            
        