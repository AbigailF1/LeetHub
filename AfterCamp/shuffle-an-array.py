class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = list(nums)
        self.nums_ = nums        

    def reset(self) -> List[int]:
        self.nums_ = self.original_nums
        self.original_nums = list(self.original_nums)
        return self.nums_
        
    def shuffle(self) -> List[int]:
        random.shuffle(self.nums_)
        return self.nums_
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()