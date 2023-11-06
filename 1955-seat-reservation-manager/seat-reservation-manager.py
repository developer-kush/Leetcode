class SeatManager:

    def __init__(self, n: int):
        self.marker = 1
        self.available = [1]

    def reserve(self) -> int:
        res = heappop(self.available)
        if res == self.marker:
            self.marker += 1
            heappush(self.available, self.marker)
        return res

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)