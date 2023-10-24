class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        poss = 0
        prev = flowerbed[0]
        for i in range(len(flowerbed) -1) :
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                poss += 1
                prev = 1
            else:
                prev = flowerbed[i]
        return poss >= n