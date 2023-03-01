class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def player(start,end,turn):
            if start == end:
                if turn:
                    return [nums[start],0]
                else:
                    return [0,nums[start]]
            if turn:
                ans1 = player(start+1,end,False)
                ans1[0]+=nums[start] 
                ans2 = player(start, end-1, False)
                ans2[0] += nums[end] 
                if ans1[0]>ans2[0]: return ans1
                return ans2
                
            else:
                ans1 = player(start+1,end,True)
                ans1[1]+=nums[start] 
                ans2 = player(start, end-1, True)
                ans2[1]+=nums[end] 
                if ans1[1]>ans2[1]: return ans1
                return ans2
        answer = player(0,len(nums)-1, True)
        if answer[0] >= answer[1]: return True
        return False 
                
        