class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        y=sorted(nums)
        
        while l<=r:
            if y[l]+y[r]==target:
                break
            elif y[l]+y[r]>target:
                r-=1
            elif y[l]+y[r]<target:
                l+=1
        if y[l]!=y[r]:
            return [nums.index(y[l]),nums.index(y[r])]   
        else:
           return [nums.index(y[l]),[i for i, n in enumerate(nums)if n==y[l]][1]]
           
            


        

            