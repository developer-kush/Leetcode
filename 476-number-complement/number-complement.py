class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        s = ''.join(map(str, [1-int(i) for i in s]))
        return int(s, 2)