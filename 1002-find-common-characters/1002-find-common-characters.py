class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        dic = defaultdict(int)
        for i in words[0]:
            dic[i] += 1
        for i in range(len(words)):
            for j in words[0]:
                counter = words[i].count(j)
                if counter < dic[j]:
                    dic[j] = counter
        for i in dic:
            while dic[i]>0:
                ans.append(i)
                dic[i]-=1
             
        return ans
        