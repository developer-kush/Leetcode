class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        curr = 0
        for move in (bin(k-1)[2:]).rjust(n, '0'):
            if move == '1': curr = 1 - curr

        return curr