class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        d_f_t = inf
        ans = 0
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) -1
            while l < r:
                tar = nums[l] + nums[r] + nums[i]
                pos = abs(target - tar)
                if pos < d_f_t:
                    d_f_t = pos
                    ans = tar
                if tar > target:
                    r -= 1
                   
                elif tar < target:
                    l += 1
                    
                elif tar == target:
                    return target

        return ans

        