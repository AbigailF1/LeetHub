class Solution:
    def isPalindrome(self, x: int) -> bool:
        Y=str(x)
        if Y==Y[::-1]:
            return True 
        else: 
            return False
        