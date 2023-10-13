# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        l = 0
        r = n - 1
        while (l < r):
            mid = (r + l) // 2
            x = mountain_arr.get(mid)
            y =  mountain_arr.get(mid + 1)   
            
            if x <  y:
                l = mid+1
            
            else:
                r = mid
        peak = l

        if mountain_arr.get(peak) == target:
            return peak
    #  below peak
        l = 0
        r = peak
        while (l < r):
            mid = (r + l) // 2
            
            x = mountain_arr.get(mid)  
            if x == target:
                return mid
            
            if x <  target:
                l = mid + 1
            
            else:
                r = mid
                
            
    # above peak
        l = peak
        r = n
        while (l < r):
            mid = (r + l) // 2

            x = mountain_arr.get(mid)  
            if x == target:
                return mid

            if x <  target:
                r = mid

            else:
                l = mid + 1
        
        return -1
        