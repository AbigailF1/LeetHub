class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:
            return None 
        def largescore(left, right):
            if left > right:
                return 0
            return max ((nums[left] - largescore(left + 1, right)), nums[right] - largescore(left, right -1))
        return largescore(0, len(nums)-1)>=0
            