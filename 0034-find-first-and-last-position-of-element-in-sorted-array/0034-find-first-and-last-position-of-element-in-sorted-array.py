class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_left):
            l = 0
            r = len(nums) - 1
            ans = -1
            print(target)
            while l <= r:
                mid = (l+r)//2
                #print([mid, nums[mid], target])
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    ans = mid
                    if is_left == True:
                        r = mid - 1
                    else:
                        l = mid + 1
              
            return ans
        left = binary_search(True)
        right = binary_search(False)
        return [left, right]

            
            
        