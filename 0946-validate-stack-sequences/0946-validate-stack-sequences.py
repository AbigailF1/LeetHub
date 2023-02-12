class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        y=0
        s=[]
        for x in pushed:
            s.append(x)
            while s and y < len(popped) and s[-1]==popped[y]:
                s.pop()
                y+=1
        return y==len(popped)
        