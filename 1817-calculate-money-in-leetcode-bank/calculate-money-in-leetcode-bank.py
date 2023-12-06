class Solution:
    def totalMoney(self, n: int) -> int:
        g, r = divmod(n, 7)
        return 7*((g<<2) + ((g*(g-1))>>1)) + ((r*(r+1 + (g<<1)))>>1) 