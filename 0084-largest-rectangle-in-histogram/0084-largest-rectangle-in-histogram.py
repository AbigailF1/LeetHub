class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        p_s = [-1]* len(heights) 
        n_s = [len(heights)] * len(heights)
        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]: 
                n_s[s[-1]] = i 
                s.pop()
            if s:
                p_s[i] = s[-1]
            s.append(i)
        area = 0
        for j in range(len(heights)):
            area = max(area, (heights[j]*(n_s[j] - p_s[j] -1)) )
            print(heights[j],n_s[j], p_s[j], area)
        return area 
                
        