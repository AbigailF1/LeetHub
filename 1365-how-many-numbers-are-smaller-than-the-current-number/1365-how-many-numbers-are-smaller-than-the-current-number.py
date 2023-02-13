class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums= sorted(nums)
        d={}
        result=[]
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in d:
                d[sorted_nums[i]]=i
        for i in nums:
            result.append(d[i])
        return result
            