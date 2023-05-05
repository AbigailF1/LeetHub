class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1* pile for pile in piles]
        heapify(piles)
        for i in range(k):
            
            x =  heappop(piles)//2
            heappush(piles, x)
        return -1* (sum(piles))
            
        