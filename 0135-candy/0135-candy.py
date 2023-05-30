class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        after = [1]*n
        before = [1]*n
       
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                after[i] = after[i + 1] + 1
        for i in range(1, n):
            if ratings[i] > ratings[i -1]:
                before[i] = before[i-1] + 1
        ans = 0
        print(after)
        print(before)
        for i in range(n):
            ans += max(after[i], before[i])
        return ans
        