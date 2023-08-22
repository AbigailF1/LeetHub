class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for scen in words:
            for word in scen.split(separator):
                if word:
                    ans.append(word)
        return ans
                
        