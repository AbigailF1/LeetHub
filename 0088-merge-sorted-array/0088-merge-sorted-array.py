class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = 0
        for i in range(m + n):
            if nums1[i] == 0:
                if l < n:
                    nums1[i] += nums2[l]
                l+=1
        return nums1.sort()

