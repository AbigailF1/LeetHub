class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        for i in nums1:
            f= False
            i_index = nums2.index(i)
            x= nums2[i_index+1:]
            for k in x:
                if k > i:
                    s.append(k)
                    f = True
                    break

            if f == False:
                s.append(-1)
        return s
        