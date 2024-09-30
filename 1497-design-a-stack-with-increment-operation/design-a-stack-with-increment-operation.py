class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.offset = 0
        self.extras = Counter()
        self.size = maxSize

    def push(self, x: int) -> None:
        self.extras[len(self.st)] += self.offset
        self.offset = 0
        if len(self.st) != self.size: self. st.append(x)

    def pop(self) -> int:
        self.offset += self.extras[len(self.st)]
        self.extras[len(self.st)] = 0
        if self.st: return self.offset + self.st.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.st): self.offset += val
        else: self.extras[k] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)