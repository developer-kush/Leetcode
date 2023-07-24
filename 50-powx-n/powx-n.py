class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            
            if n == 0: return 1
            if n == 1: return x
            sol = rec(x,n>>1)
            if n&1: return sol*sol*x
            else: return sol*sol

        if n<0: return 1/rec(x,-n)
        return rec(x,n)