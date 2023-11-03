class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag1 = True 
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                flag1 = False
        flag2 = True
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                flag2 = False

        return flag1 or flag2
                

        