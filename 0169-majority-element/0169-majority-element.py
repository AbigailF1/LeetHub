class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        ans = 0
        for key, val in dic.items():
            if val > n/2:
                ans = key
        return ans
        