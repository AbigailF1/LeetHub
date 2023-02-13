class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort()
        ans=[intervals[0]]
        for x,y in intervals[1:]:
            if x>ans[-1][1]:
                ans.append([x,y])
            elif y>ans[-1][1]:
                ans[-1][1]=y
        return ans