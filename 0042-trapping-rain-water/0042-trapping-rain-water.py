class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        ans = 0
        for i in range(len(height)):
            while s and s[-1][1] <= height[i]:
                popped = s.pop()
                if s:
                    h = min(height[i], s[-1][1]) - popped[1]
                    width = i - s[-1][0] - 1
                    ans += (h*width) 
            s.append([i, height[i]])
        return ans
            
        