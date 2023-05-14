class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0 or k == len(nums):
            return nums
        x = nums[-k:]
        y = nums[:-k]
        nums[:k] = x
        nums[k:] = y
            
        