class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        for i in dic:
            if dic[i] == 1:
                return i
            