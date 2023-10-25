class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k-=1
        tot = False
        while k:
            k &= (k-1)
            tot = not tot
        return int(tot)