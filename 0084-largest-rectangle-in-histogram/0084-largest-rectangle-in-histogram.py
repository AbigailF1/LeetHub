class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        s = []
        p_s = [-1]* length
        n_s = [length] * length
        for i in range(length):
            while s and heights[s[-1]] > heights[i]: 
                n_s[s[-1]] = i 
                s.pop()
            if s:
                p_s[i] = s[-1]
            s.append(i)
        area = 0
        for j in range(length):
            area = max(area, (heights[j]*(n_s[j] - p_s[j] -1)) )
        return area 
                
        