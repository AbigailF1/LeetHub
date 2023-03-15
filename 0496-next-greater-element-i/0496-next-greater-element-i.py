class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        next_greater = [-1] * len(nums1)
        for i in range(len(nums2)):
            
            while s and nums2[s[-1]] < nums2[i]:
                if nums2[s[-1]] in nums1:
                    i_index = nums1.index(nums2[s[-1]])
                    next_greater[i_index] = nums2[i]  
                s.pop()
            s.append(i)
        return next_greater
                
                
                
                
                
                