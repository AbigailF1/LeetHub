class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(arr, low, high):
            pivot = arr[high]
            i = low -1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j]= arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            
            return i+1
        def quicksort(arr, low, high):
            if low < high:
                part = partition(arr, low, high)
                quicksort(arr, low, part - 1)
                quicksort(arr, part + 1, high)
        
        quicksort(nums, 0, len(nums)-1)
        ans = []
        Count = Counter(nums)
        count = [(l,k) for k,l in sorted([(j,i) for i,j in Count.items()], reverse=True)]
        for i in range(k):
            ans.append(count[i][0])
        return ans    
      