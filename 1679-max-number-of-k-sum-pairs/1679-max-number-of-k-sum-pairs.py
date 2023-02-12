class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mi = defaultdict(int)
        ans = 0
        for x in nums: mi[x] += 1
        for x in nums:
          if mi[x] < 1 or mi[k - x] < 1 + (x + x == k): 
            continue
          mi[x] -= 1
          mi[k - x] -= 1
          ans += 1
        return ans   