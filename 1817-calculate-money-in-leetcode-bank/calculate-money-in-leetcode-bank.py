class Solution:
    def totalMoney(self, n: int) -> int:
        g, r = divmod(n, 7)
        return (g*28+7*((g*(g-1))>>1)) + ((r*(r+1))>>1) + g*r