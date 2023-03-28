class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        possible_pairs = 0
        def merge(arr):
            nonlocal possible_pairs 
            if len(arr) == 1:
                return arr
            left = merge(arr[:len(arr)//2])
            right = merge(arr[len(arr)//2:])
            print (right)
            for i in left:
                possible_pairs += bisect_left(right, i/2)
            
            ans = []
            l = r = 0
            while r < len(right) or l < len(left):
                
                if r >= len(right) or ((l < len(left)) and (left[l] <= right[r])):
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            return ans 
        merge(nums)
        return possible_pairs 
            
        