
from bisect import insort

class MedianFinder:

    def __init__(self):
        self.hp = []

    def addNum(self, num: int) -> None:
        insort(self.hp, num)

    def findMedian(self) -> float:
        ln = len(self.hp)
        median = self.hp[ln//2]
        if not ln&1:
            median = (median + self.hp[ln//2 - 1])/2
        return median
        
# 1 2 3 4 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()