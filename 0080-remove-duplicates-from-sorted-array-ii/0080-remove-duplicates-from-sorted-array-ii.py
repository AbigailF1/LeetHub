class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[ptr-2]:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr
        