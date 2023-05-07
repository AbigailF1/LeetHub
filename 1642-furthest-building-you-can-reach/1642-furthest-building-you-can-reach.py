class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ans = []
        bricks_used = 0
        for i in range(len(heights) - 1):
            if heights[i+1] < heights[i]:
                continue
            if heights[i+1] > heights[i]:
                height = heights[i+1] - heights[i]
                if len(ans) < ladders:
                    heappush(ans, height)
                else:
                    bri = heappushpop(ans, height)
                    bricks_used += bri
            if bricks_used > bricks:
                return i 
        return len(heights) - 1
        