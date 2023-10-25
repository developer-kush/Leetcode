class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k-=1
        tot = 0
        while k:
            k &= (k-1)
            tot += 1
        return tot&1