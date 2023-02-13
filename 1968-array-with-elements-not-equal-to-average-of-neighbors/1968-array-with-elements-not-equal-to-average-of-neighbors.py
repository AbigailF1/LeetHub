class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        l,r=0,len(nums)-1
        while len(arr)!=len(nums):
            arr.append(nums[l])
            l+=1
            if l<=r:
                arr.append(nums[r])
                r-=1
        return arr