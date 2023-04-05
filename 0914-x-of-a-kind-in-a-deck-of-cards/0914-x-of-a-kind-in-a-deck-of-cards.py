class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = list(Counter(deck).values())   
        g = count[0]
        for j in range(len(count)):
            if count[j] == 1:
                return False
            else:  
                g = gcd(g, count[j]) 
        if g > 1:
            return True 
        else:
            return False
           
           
        