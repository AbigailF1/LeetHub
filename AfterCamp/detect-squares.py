class DetectSquares:

    def __init__(self):
        self.dictionary = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.dictionary[(x,y)]+=1
        
    def count(self, point: List[int]) -> int:
        count = 0
        x1 , y1 = point
        for x,y in self.dictionary.keys():
            if(abs(x1-x)==abs(y1-y) and  y1-y != 0 ):
                possible_point1 = (x1,y)
                possible_point2 = (x,y1)

                if(possible_point1 in self.dictionary and possible_point2 in self.dictionary):
                    count +=self.dictionary[(x,y)]*self.dictionary[possible_point1]*self.dictionary[possible_point2]

        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)