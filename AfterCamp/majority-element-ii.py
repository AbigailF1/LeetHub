class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = floor(len(nums)/3)
        count = Counter(nums)

        ans = []
        for key, values in count.items():
            if values > target:
                ans.append(key)
        return ans