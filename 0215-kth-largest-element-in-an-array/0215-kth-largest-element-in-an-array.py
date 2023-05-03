class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapify(arr)
        for i in range(k):
            heappush(arr, nums[i])
        for i in range(k, len(nums)):
            heappushpop(arr, nums[i])
        return arr[0]
     
        

        