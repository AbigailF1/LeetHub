class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        new = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                new += word1[i]
                i += 1
            else:
                new += word2[j]
                j += 1

        new += word1[i:] + word2[j:]

        return new