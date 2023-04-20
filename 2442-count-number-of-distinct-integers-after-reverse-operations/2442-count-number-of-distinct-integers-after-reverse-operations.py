class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        for i in nums:
            ans.add(int(str(i)[::-1])) 
        return len(ans)
            
            
        