class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans  = set()
        def backtrack(nums, indx, res):
            nonlocal ans
            if len(res) >=2:
                    ans.add(tuple(res))
            if indx == len(nums):
                return 
            for i in range(indx, len(nums)):
                if (not res or nums[i] >= res[-1]):
                    res.append(nums[i])
                    backtrack(nums, i+1, res)
                    res.pop()
                
            return 
        backtrack(nums, 0, [])
        return ans


            
        