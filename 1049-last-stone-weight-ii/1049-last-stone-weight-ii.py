class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}
        summ = sum(stones)
        targ_summ = ceil(summ/2)
        
        def recc(indx, tot_sum):
            if tot_sum >= targ_summ:
                return abs(tot_sum - (summ - tot_sum))
            
            if indx == len(stones):
                return abs(tot_sum - (summ - tot_sum))
            
            if (indx, tot_sum) in memo:
                return memo[(indx, tot_sum)]
            
            
            memo[(indx, tot_sum)]= min(recc(indx +  1, tot_sum + stones[indx] ), recc(indx +  1, tot_sum ))
            return memo[(indx, tot_sum)]
        
        return recc(0,0)