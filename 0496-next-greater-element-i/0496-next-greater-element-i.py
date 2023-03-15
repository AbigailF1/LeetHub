class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        next_greater = defaultdict(int)
        for i in range(len(nums2)):
            while s and nums2[s[-1]] < nums2[i]:
                next_greater[nums2[s[-1]]] = nums2[i]  
                s.pop()
            s.append(i)
        ans = [-1]* len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                ans[i] = next_greater[nums1[i]] 
        return ans
                
                
                
                
                
                