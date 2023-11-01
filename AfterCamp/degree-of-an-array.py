class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_ = 1
        degree_nums = set()
        indexs = defaultdict(list)
        for key, values in count.items():
            max_ = max(max_, values)
        for key, value in count.items():
            if value == max_:
                degree_nums.add(key)
        for i in range(len(nums)):
            indexs[nums[i]].append(i)
        ans = float("inf")
        
        for num in degree_nums:
            ans = min(ans,  max(indexs[num]) - min(indexs[num]) + 1)
        return ans 


        
        
        


        