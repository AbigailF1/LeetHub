class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = len(strs)
        for i in range(len(strs[0])):
            for j in range(len(strs) -1):
                if strs[j][i] > strs[j+1][i]:
                    delete -= 1
                    break
        return len(strs) - delete
                
            