class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(indx, track):
            if indx >= n:
                ans.append(track)
                return 
            backtrack(indx+1,track)
            backtrack(indx+1, track +[nums[indx]])
        
            
        n = len(nums)
        backtrack(0, [])
        return ans
    