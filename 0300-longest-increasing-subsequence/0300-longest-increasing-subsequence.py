class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        poss = []
        for num in nums:
            if len(poss) == 0 or poss[-1] < num:
                poss.append(num)
            else:
                poss[bisect_left(poss,num)] = num
                
        return len(poss)
        