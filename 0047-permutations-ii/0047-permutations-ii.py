class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(num, List):
            if len(num) == len(nums):
                ans.add(tuple(num.copy()))
                return
            for i in range(len(List)):
                num.append(List[i])
                backtrack(num, List[:i] + List[i+1:])
                num.pop()
        backtrack([], nums)
        return list(ans)
            