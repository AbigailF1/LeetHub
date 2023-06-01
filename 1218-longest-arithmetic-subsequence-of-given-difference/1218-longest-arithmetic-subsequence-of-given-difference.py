class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        for i in range(len(arr)):
            memo[arr[i]] = max(memo[arr[i]-difference] + 1, memo[arr[i]])
        return(max(list(memo.values())))
                
                
        