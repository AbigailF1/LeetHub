class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        for i in words[-1]:
            for j in range(len(words)):
                if i not in words[j]:
                    break
                words[j] = words[j].replace(i, "", 1)  
                
            else:
                res.append(i)
        return res