class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        ans = [-1]* len(nums) 
        for j in range(2):
            for i in range(len(nums)):
                while s and nums[s[-1]] < nums[i]: 
                    ans[s[-1]] =nums[i] 
                    s.pop()
                s.append(i)
        return ans 
        
                
                
        