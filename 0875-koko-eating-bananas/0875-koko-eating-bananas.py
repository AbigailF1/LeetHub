class Solution:
    def check_if_true(self, banana_piles, mid_val, H):
        time = 0
        for i in range(len(banana_piles)):
            if banana_piles[i] % mid_val != 0:
                time += (banana_piles[i] // mid_val) + 1
            else:
                time += (banana_piles[i] // mid_val) 
        if time <= H:
             return True 
        else:
             return False          
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest  = 1 
        highest = max(piles)        
        while lowest < highest :
            mid = lowest + (highest - lowest)//2
            if self.check_if_true(piles, mid, h) == True:
                highest = mid 
            else:
                lowest = mid + 1 
        return lowest
                    