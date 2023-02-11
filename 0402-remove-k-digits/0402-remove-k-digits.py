class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l,length=0,len(num)
        s=[]
        if k>=length:
            return "0"
        while l<length:
            while (s and k>0) and(int(s[-1])>int(num[l])):
                s.pop()
                k-=1
            s.append(num[l])
            l+=1
        while k>0:
            s.pop()
            k-=1
        return str(int("".join(s)))