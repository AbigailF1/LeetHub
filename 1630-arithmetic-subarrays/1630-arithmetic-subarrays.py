class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            l_index = l[i]
            r_index = r[i]
            x = nums[l_index:r_index+1]
            x.sort()
            if(len(x)==2):
                ans.append(True)
                continue
            distance = x[1]-x[0]
            for j in range(2, len(x)):
                if distance != x[j]-x[j-1]:
                    ans.append(False)
                    break
                elif j==len(x)-1:
                    ans.append(True)
        return ans       	      
