class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        l = 0
        r = len(nums) -1
        ans = [-1,-1]
        nums.sort()
        while (l < r):
            print(l,r)
            if nums[l] + nums[r] ==  target:
                ans[0] = nums[l]
                ans[1] = nums[r]
                break 
            elif nums[l] + nums[r] <  target:
                l += 1
            else:
                r -= 1
        # print(ans)
        if ans[0] == ans[1]:
            return dic[ans[0]]
        else:
            return [dic[ans[0]][0], dic[ans[1]][0]]