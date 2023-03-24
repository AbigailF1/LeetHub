class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            correct_position = nums[i] -1
            if correct_position != i and nums[correct_position] != nums[i]:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        arr = []
        for j in range(len(nums)):
            if j+1 != nums[j]:
                arr.append(j+1)
        return arr
