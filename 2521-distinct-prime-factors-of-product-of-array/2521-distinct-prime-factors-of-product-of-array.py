class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
     
        count = set()       
        # def is_prime(x):
        #     d = 2
        #     while d * d <= x:
        #         if x % d == 0:
        #             return False
        #         d += 1
        #     return True
        
        for i in range(len(nums)):
            number = int(math.sqrt(nums[i]))
            for j in range(2, number+1):
                if nums[i] % j == 0:
                    count.add(j)
                    while nums[i] % j == 0: 
                        nums[i] //= j
            if (nums[i] >= 2):
                count.add(nums[i])
        
        return len(count)
    
        