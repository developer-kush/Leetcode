class Solution:
    def minEnd(self, n: int, x: int) -> int:
        indices = []
        for i in range(0, 32):
            if not x: break
            if x&1: indices.append(i)
            x >>= 1

        num = bin(n-1)[:1:-1]
        
        res = ""
        y = 0
        for ch in num:
            while y < len(indices) and len(res) == indices[y]: res += '1'; y += 1
            res += ch
        while y < len(indices):
            while len(res) < indices[y]: res += '0'
            res += '1'
            y += 1

        return int(res[::-1], 2)