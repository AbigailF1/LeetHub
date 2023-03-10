class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = 0
        max_count = 0
        l = 0
        count = collections.Counter()
        for r , c in enumerate(s):
            count[c] +=1
            max_count = max(max_count, count[c])
            while max_count + k < r - l + 1:
                count[s[l]]-=1
                l+=1
            res = max(res, r - l + 1)
        return res 