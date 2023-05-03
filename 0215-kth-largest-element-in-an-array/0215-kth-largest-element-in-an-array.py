class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * i for i in nums]
        heapify(nums)
        for i in range(1, k):
            heappop(nums)
        return heappop(nums) * (-1)
        

        