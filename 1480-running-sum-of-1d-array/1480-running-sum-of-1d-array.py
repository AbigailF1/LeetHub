class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        output = []
        for i in range(len(nums)):
            prefix_sum += nums[i]
            output.append(prefix_sum)
        return output 