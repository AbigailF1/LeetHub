class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:               
        ans = []
        def backtrack(num, List):
            if len(num) == len(nums):
                ans.append(num.copy())
                return
            else:                
                for i in range(len(List)): 
                    num.append(List[i])
                    backtrack(num, List[:i] + List[i+1:])
                    num.pop()
        backtrack([], nums)
        return ans
                

        