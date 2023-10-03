class MyCalendar:

    def __init__(self):
        self.booked = []
        

    def book(self, start: int, end: int) -> bool:
        for st, en in self.booked:
            if start < en and st < end:
                return False 
        self.booked.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)