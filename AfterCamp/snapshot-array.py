class SnapshotArray:
    def binary_search(self, l, r , target, _list):
        point = 0
        while l <= r:
            mid = (l + r) // 2
            if _list[mid][1] <= target:
                point = mid
                l = mid + 1
            else:
                r = mid - 1
        return point 

    def __init__(self, length: int):
        self.arr = [0] * length 
        self.snap_shot = 0
        self.dic = [[(0,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        if self.dic[index][-1][1] == self.snap_shot:
            self.dic[index][-1] = (val, self.snap_shot)
        elif self.dic[index][-1][1] < self.snap_shot:
            self.dic[index].append((val, self.snap_shot))

        
    def snap(self) -> int:   
        self.snap_shot += 1
        return self.snap_shot - 1  
                 
    def get(self, index: int, snap_id: int) -> int:
        ans = self.binary_search(0, len(self.dic[index]) - 1 , snap_id, self.dic[index])
        return self.dic[index][ans][0]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)