class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            words=tuple(sorted(list(i)))
            d[words].append(i)
        return d.values()
        