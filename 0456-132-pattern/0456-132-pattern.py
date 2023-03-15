class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimum = float('-inf')
        s = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < minimum:
                return True
            while s and s[-1] < nums[i]:
                minimum = s.pop()
            s.append(nums[i])
        return False
            