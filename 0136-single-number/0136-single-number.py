class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
        for key, val in dic.items():
            if val == 1:
                return key