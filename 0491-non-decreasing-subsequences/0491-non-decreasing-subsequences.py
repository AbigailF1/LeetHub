class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        def backtrack(nums, indx, res):
            nonlocal ans
            visited = set()
            if len(res) >=2:
                    ans.append(res.copy())
            if indx == len(nums):
                return 
            for i in range(indx, len(nums)):
                if (nums[i] not in visited) and (not res or nums[i] >= res[-1]):
                    res.append(nums[i])
                    backtrack(nums, i+1, res)
                    res.pop()
                visited.add(nums[i])
            return 
        backtrack(nums, 0, [])
        return ans


            
        