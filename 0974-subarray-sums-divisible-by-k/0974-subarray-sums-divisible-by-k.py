class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        dic = defaultdict(int)
        dic[0] = 1
        presum = 0
        arr = []
        for i in nums:
            presum += i
            arr.append(presum)
        for j in arr:
            r = j % k
            if r in dic:
                ans += dic[r]
            dic[r] += 1
        #print(dic)
        return ans
        
            
        