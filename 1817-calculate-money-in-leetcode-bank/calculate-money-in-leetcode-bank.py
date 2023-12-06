class Solution:
    def totalMoney(self, n: int) -> int:
        g, r = divmod(n, 7)
        additive = (g*(g-1))>>1
        return 7*((g<<2) + additive) + ((r*(r+1 + (g<<1)))>>1) 