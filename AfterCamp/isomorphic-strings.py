class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {i: -1 for i in s}
        used = set()
        for i in range(len(s)):
            if dic[s[i]] == -1 and t[i] not in used:
                dic[s[i]] = t[i]
                used.add(t[i])
        
        for i in range(len(s)):
            if dic[s[i]] != t[i]:
                return False
        return True
            
        