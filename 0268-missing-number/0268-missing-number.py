class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_new = set(nums)
        for i in range(len(nums_new) + 1):
            if i not in nums:
                return i 