class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0,len(nums)-1):
            min=i
            for j in range(i+1,(len(nums))):
                if nums[j]<nums[min]:
                    min=j
            if min!=i:
                nums[i],nums[min]=nums[min],nums[i]
