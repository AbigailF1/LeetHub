class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i,r in enumerate(nums):
            if left_sum== total-r-left_sum:
                return i 
            left_sum+=r
        return -1