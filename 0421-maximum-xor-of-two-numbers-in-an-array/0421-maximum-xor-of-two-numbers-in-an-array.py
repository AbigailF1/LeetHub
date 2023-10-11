class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0,0
        for i in range(32, -1,-1):
            mask = mask|1<<i
            found = set([n & mask for n in nums])
            
            temp = output|1 << i
            for ele in found:
                if ele^temp in found:
                    output = temp
        return output
            