class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for val in count.values():
            if val!= 1:
                ans += (val * (val - 1) )// 2
        return ans 
        