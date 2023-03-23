class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        s_nums = set(range(1,len(nums)+1))
        ans.append(mode(nums))
        x = set(nums)
        ans += list(s_nums - x)
        return ans 