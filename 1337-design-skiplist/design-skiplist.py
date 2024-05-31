class Skiplist:

    def __init__(self):
        self.d = {}

    def search(self, target: int) -> bool:
        return target in self.d and self.d[target] > 0

    def add(self, num: int) -> None:
        self.d[num] = self.d.get(num, 0) + 1

    def erase(self, num: int) -> bool:
        if num in self.d and self.d[num] > 0:
            self.d[num] -= 1
            return True
        else: return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)