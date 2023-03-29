class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        new_nums = [(nums[i],i) for i in range(len(nums))]
        
        dic = defaultdict(int)
        
        def merge(new_nums): 
            nonlocal dic
            if len(new_nums) == 1:
                return new_nums
            
            left = merge(new_nums[:len(new_nums)//2])
            right = merge(new_nums[len(new_nums)//2:])
            
            ans = []
            l = r = 0
            while r < len(right) or l < len(left):
                
                if r >= len(right) or ((l < len(left)) and (left[l][0] <= right[r][0])):
                    dic[left[l][1]] += len(ans) - l                   
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            return ans
        merge(new_nums)
        arr = []
        for i, j in sorted(dic.items()):
            arr.append(j)
        return arr + [0]
            