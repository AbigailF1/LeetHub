class Solution:
    def minTimeToType(self, word: str) -> int:
        dic = {chr(i + 96): i for i in range(1, 27)}
        prev = "a"
        ans = 0
        for let in word:
            dist = abs(dic[prev] - dic[let])
            ans += min(dist , 26 - dist) + 1
            prev = let
        return ans

        