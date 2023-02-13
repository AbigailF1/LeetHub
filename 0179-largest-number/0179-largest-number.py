class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, j in enumerate(nums):
            nums[i]=str(j)
        def compare(j1, j2):
            if j1+j2>j2+j1:
                return -1
            else:
                return 1

        nums=sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))

