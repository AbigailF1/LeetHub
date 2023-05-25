class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        minn = nums[0]
        midd = inf
        for i in range(len(nums)):
            if nums[i] <= minn:
                minn = nums[i]
            elif nums[i] < midd:
                midd = nums[i]
            elif nums[i] > midd > minn:
                return True
        return False
            
        