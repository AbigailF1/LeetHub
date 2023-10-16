class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sum_even, sum_odd = 0,0
        
        for i in range(len(nums) -1, -1, -1):
            temp_o = max(sum_even - nums[i], sum_odd)
            temp_e = max(sum_odd + nums[i], sum_even)
            
            sum_even, sum_odd = temp_e, temp_o
        
        return sum_even