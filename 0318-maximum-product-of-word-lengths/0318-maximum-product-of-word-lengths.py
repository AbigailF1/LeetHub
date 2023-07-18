class Solution:
    def maxProduct(self, words: List[str]) -> int:
        new_words = [0]*len(words)
        for i in range(len(words)):
            for l in words[i]:
                new_words[i] |= (1 << (ord(l) - 97))
        # print(new_words)
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if new_words[i] & new_words[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
        