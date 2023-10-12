class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        map_ = {}
        mod_ = sum(nums) % p
        
        if mod_ == 0:
            return 0 
        n = len(nums)
        ans = n
        sum_ = 0
        map_[0] = -1
        
        for i in range(n):
            sum_ += nums[i]
            key = ((sum_ % p) - mod_)
            
            if key < 0:
                key%= p
            
            if key in map_:
                ans = min(ans, i - map_[key])
            map_[sum_%p] = i
            
        return ans if ans < n else -1 
        
        