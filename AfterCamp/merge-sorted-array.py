class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m -1 
        r = n - 1
        k = m + n - 1

        while r >= 0:
            if l >= 0 and nums1[l] > nums2[r]:
                nums1[k] = nums1[l]
                k -= 1
                l -= 1
            else:
                nums1[k] = nums2[r]
                k -= 1
                r -= 1
        
        
        