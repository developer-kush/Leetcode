class MyCalendarTwo:
    
    def __init__(self):
        self.cnts = Counter()

    def book(self, start: int, end: int) -> bool:
        self.cnts[start] += 1
        self.cnts[end] -= 1

        cnt = 0
        for key in sorted(self.cnts):
            cnt += self.cnts[key]
            if cnt >= 3: break

        if cnt < 3: return True
        else: 
            self.cnts[start] -= 1
            self.cnts[end] += 1
            return False
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)