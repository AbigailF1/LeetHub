class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i, j in enumerate(nums):
            for x in nums[i+1:]:
                if x==j:
                    count+=1
        return count

            
