class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = list(accumulate(nums))

        ans = 0
        count = defaultdict(int)
        count[0] = 1

        for n in pre_sum:
            diff = n % k 
            ans += count[diff]
            count[diff] += 1
        return ans