class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = i = 0
        count = collections.Counter()
        for j, n in enumerate(fruits):
            count[n] += 1
            while len(count) >= 3:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
        