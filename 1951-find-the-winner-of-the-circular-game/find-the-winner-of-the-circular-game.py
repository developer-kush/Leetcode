class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def rec(n, k):
            if n == 1: return 1

            next = (k-1)%n + 1

            winner = rec(n-1, k)
            winner+=next

            return (winner-1)%n+1
        
        return rec(n, k)
            