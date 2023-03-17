class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(indx, track):
            if indx >= n:
                ans.append(track.copy())
                return 
            track.append(nums[indx])
            backtrack(indx+1, track)
            track.pop()
            backtrack(indx+1, track)
        n =len(nums)
        backtrack(0, [])
        return ans 