
from bisect import insort

class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if self.hi and num >= self.hi[0]: heappush(self.hi, num)
        else: heappush(self.lo, -num)

        if len(self.hi)-len(self.lo) >= 2: heappush(self.lo, -heappop(self.hi) )
        if len(self.lo)-len(self.hi) >= 2: heappush(self.hi, -heappop(self.lo) )

    def findMedian(self) -> float:
        if len(self.lo)> len(self.hi): return -self.lo[0]
        elif len(self.hi) > len(self.lo): return self.hi[0]
        else: return (self.hi[0]-self.lo[0])/2

# 7 - ___ -> 7
# 3 7 - ___ -> 3 - 7 
# 3 - 7 13 -> 7



# 1. if ln(h1)-ln(hp2)>=2 move 1 element to hp2 ( balance both )
# 2. if ln(hp1) - ln(hp2) == 1 or 0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()