class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
              
        for i in range (1, len(strs)):
            j = 0
            new_pre = ""
            for lett in strs[i]:
                if j < len(prefix) and lett == prefix[j]:
                    new_pre += lett
                else:
                    break
                j += 1
            prefix = new_pre
        return prefix
           