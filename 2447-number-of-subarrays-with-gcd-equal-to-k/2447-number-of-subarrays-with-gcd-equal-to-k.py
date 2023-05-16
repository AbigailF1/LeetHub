class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def GCD(x , y):
            if y == 0:
                return x
            r = int(x % y)
            return GCD(y , r)
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i, len(nums)):
                num = GCD(num, nums[j])
                if num == k:
                    ans += 1
                elif num < k:
                    break    
        return ans 
            