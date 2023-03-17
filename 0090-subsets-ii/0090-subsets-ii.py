class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(indx, track):
            if indx >= n:
                ans.append(track.copy())
                return 
            track.append(nums[indx])
            backtrack(indx+1, track)
            while indx < n-1 and nums[indx]== nums[indx+1]:
                indx+=1
            track.pop()
            backtrack(indx+1, track)
            
        n = len(nums)
        backtrack(0, [])
        return ans
        