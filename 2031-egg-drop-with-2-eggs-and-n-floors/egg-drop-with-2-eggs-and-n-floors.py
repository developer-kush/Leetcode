class Solution:
    def twoEggDrop(self, n: int) -> int:
        tot = 0
        for i in range(1, 50):
            tot += i
            if tot >= n: break
        return i