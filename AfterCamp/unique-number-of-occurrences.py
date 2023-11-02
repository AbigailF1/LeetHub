class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        unique = list(count.values())
        return len(set(unique)) == len(unique)
        