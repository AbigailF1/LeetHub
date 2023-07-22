class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        s = s.strip()
        for i in range(len(s)):
            if s[i]!= " ":
                last_word += s[i]
            else:
                last_word = ""
        return len(last_word)
        