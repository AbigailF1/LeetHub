class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append (-1)
        n = len(nums)
        i = 0
        while i < n:
            correct_position = nums[i]
            if nums[i]!= -1 and correct_position != i:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        for j in range(len(nums)):
            if nums[j] == -1:
                return j

