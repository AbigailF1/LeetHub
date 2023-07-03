class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = []
        def back(start, num, arr):
            # print(num)
            ans.append(num)
            for i in range(start, len(arr)):
                back(i + 1, num|nums[i], arr)
        back(0,0,nums)
        count = Counter(ans)
        res = max(count.values())
        return res