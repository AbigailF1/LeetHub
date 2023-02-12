class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)//3
        p = [[piles[2*i], piles[2*i+1], piles[-i-1]] for i in range(n)]
        return sum([j[1] for j in p])
        