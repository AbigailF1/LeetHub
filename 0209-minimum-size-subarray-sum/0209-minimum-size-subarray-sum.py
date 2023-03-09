class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        sums = nums[0]
        min_length = len(nums)
        if sum(nums) < target:
            return 0
        while r < len(nums):
            if sums < target:
                r += 1
                if not r < len(nums):
                    break
                sums += nums[r]
            else:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                sums -= nums[l]
                l += 1
        return min_length
            

        
        