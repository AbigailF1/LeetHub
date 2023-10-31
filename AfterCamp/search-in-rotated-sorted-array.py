class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find rotating pivot 
        l , r = 0, len(nums) - 1
        while (l < r):
            mid = (r + l) // 2
            if mid < r and nums[mid] > nums[mid + 1]:
                l = mid 
                break
            if mid > l and nums[mid] < nums[mid - 1]:
                l = mid - 1
                break
            
            elif nums[mid] > nums[l]:
                l = mid + 1
            
            else:
                r = mid
        
        peak = l
        if nums[peak] == target:
            return peak
        
        # below pivot 
        l, r = 0, peak
        while (l < r):
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        # above pivot
        l, r = peak + 1, len(nums)
        while (l < r):
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
            
        return -1



        