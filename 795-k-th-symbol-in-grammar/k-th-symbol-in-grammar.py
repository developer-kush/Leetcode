class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k-=1
        tot = 0
        while k:
            if k&1: tot = 1 - tot
            k >>= 1
        return tot