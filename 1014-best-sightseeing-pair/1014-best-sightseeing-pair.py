class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr = 0
        maxx = 0
        for i in range(1, len(values)):
            curr = max(curr, values[i-1] + i-1)
            maxx = max(maxx, curr + values[i] - i)
        return maxx
            
        