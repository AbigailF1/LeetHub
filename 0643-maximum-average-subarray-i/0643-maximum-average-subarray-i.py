class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        Sum = sum(nums[:k])
        max_sum = Sum
        while r<len(nums)-1:
            r+=1
            Sum=Sum-nums[l] + nums[r]
            
            l+=1
            max_sum = max(Sum, max_sum)
        return max_sum/k