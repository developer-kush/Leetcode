class RandomizedSet:

    def __init__(self):
        self.vals = {}
        self.choices = []

    def insert(self, val: int) -> bool:
        if val in self.vals: 
            return False
        self.vals[val]=len(self.choices)
        self.choices.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        item_idx = self.vals[val]
        last = len(self.choices)-1
        self.choices[item_idx],self.choices[last]=self.choices[last],self.choices[item_idx]
        self.vals[self.choices[item_idx]] = item_idx
        del self.vals[self.choices[last]]
        self.choices.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.choices)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()