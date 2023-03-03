class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x
        while l < r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                r = mid
            if mid ** 2 < x:
                l = mid
                if mid**2 == x:
                    return mid
                    #mid = (l + r) // 2
                elif (mid+1)**2 > x:
                    return mid
        return l
                
                    
                    
                