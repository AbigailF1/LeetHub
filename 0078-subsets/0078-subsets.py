class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start, nums, track):
            
            ans.append(track[::])
            if len(track) >= n:
                return 
        
            for i in range(start, len(nums)): 
                track.append(nums[i])
                backtrack(i,nums[:i] + nums[i+1:],track)
                track.pop()
        n = len(nums)
        backtrack(0, nums, [])
        return ans
      
        
        