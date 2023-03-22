class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        max_arr = 0
        for i in range(len(arr) - 1):
            if (i%2 == 0 and arr[i] > arr[i+1]) or (i%2 == 1 and arr[i] < arr[i+1]):
                ans +=1
            else:
                ans = 0
            if ans > max_arr:
                max_arr = ans 
        ans = 0
        max_arr2 = 0
        for i in range(len(arr) - 1):
            if (i%2 == 0 and arr[i] < arr[i+1]) or (i%2 == 1 and arr[i] > arr[i+1]):
                ans +=1
            else:
                ans = 0
            if ans > max_arr2:
                max_arr2 = ans 
        return max(max_arr, max_arr2) + 1
            
        