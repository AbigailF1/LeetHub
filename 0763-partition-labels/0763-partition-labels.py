class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        ans = []
        while l < len(s):
            r = s.rfind(s[l])
            i = l + 1
            
            while i < r:
                value = s.rfind(s[i])
                r = max(r, value)
                i += 1
            
            ans.append(r - l + 1)
            l = r + 1
        return ans