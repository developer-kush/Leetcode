class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1: return 1

        pow = 1
        l, r = 1, n
        turn = 0
        num = n

        while l < r:
            if not turn:
                l += pow
                if num & 1: r -= pow
            else:
                r -= pow
                if num & 1: l += pow
            pow <<= 1
            num >>= 1
            turn = 1 - turn
        
        return l