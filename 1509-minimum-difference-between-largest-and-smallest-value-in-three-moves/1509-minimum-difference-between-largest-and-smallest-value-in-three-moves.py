class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0  
        l = 0
        r = -4
        move = 0
        ans = inf
        while move < 4:
            ans = min(ans, nums[r] - nums[l])
            l += 1
            r += 1
            move += 1
        return ans
        