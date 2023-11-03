class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0,  n-1
        if n == 1:
            return 0
        while left <= right:
            mid = (left + right)//2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            elif mid == n -1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
            else:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    if nums[mid] < nums[mid + 1]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
        