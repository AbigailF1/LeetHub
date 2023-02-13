class Solution:
    def sortSentence(self, s: str) -> str:
        word=s.split(' ')
        sentence=''
        for i in range(len(word)):
            min=i
            for j in range(i+1, len(word)):
                if word[j][-1]<word[min][-1]:
                    min=j
            if min!=i:
                word[min],word[i]=word[i],word[min]
            sentence+= word[i][:-1]+ ' '
        return sentence[:-1]