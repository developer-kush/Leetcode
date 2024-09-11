class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(abs(int(a)-int(b)) for a, b in zip(bin(start)[2:].rjust(32,'0'),bin(goal)[2:].rjust(32,'0')))