class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quick_select(l,r):
            pivot, j = nums[r], l
            
            for i in range(l,r):
                
                if nums[i] <= pivot:
                    nums[i],nums[j] = nums[j], nums[i]
                    j += 1
                
            nums[j],nums[r] = nums[r], nums[j] 

            if j > k: 
                return quick_select(l,j-1)
            elif j < k:
                return quick_select(j + 1,r)
            else:
                return nums[j]
        return quick_select(0,len(nums)- 1)

        