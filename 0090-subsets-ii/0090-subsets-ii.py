class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        def backtrack(indx, track):
            if indx >= n:
                ans.add(tuple(track))
                return 
            backtrack(indx+1,track)
            backtrack(indx+1, track +[nums[indx]])
        
            
        n = len(nums)
        backtrack(0, [])
        return list(ans)
        