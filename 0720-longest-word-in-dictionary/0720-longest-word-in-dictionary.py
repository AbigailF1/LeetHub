class Solution:
    def longestWord(self, words: List[str]) -> str:
        answer = ""
        possible_ans = set(words)
        for word in words:
            if len(word) > len(answer) or len(word) == len(answer) and word < answer:
                if all(word[:k] in possible_ans for k in range(1, len(word))):
                    answer = word

        return answer