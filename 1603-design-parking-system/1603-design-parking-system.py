class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_space = big
        self.mid_space = medium
        self.small_space = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_space > 0:
                self.big_space -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.mid_space > 0:
                self.mid_space -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.small_space > 0:
                self.small_space -= 1
                return True
            else:
                return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)