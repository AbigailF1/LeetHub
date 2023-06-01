class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        
        for i in range(len(arr)):
            if arr[i]-difference not in memo:
                memo[arr[i]] = 1
            else:
                if arr[i] not in memo:
                    memo[arr[i]] += memo[arr[i]-difference] + 1
                else:
                    memo[arr[i]] = max(memo[arr[i]-difference] + 1, memo[arr[i]])
        # print(memo)
        return(max(list(memo.values())))
                
                
        