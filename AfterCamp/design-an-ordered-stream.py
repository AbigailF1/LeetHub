class OrderedStream:

    def __init__(self, n: int):
        self. nums = ["" for i in range(n)] 
        self.n = n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.nums[idKey -1] = value
        ans = []
        for i in range (self.ptr, self.n):
            if self.nums[i] == "":
                return ans
            ans.append(self.nums[i])
            self.ptr = i + 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)