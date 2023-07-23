class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins = sorted(coins)
        
        @cache
        def rec(pos, n): # RETURNS # of ways to make n amount using coins left of position p
            
            if n == 0: return 1
            if pos < 0 or n < 0: return 0

            take = rec(pos, n-coins[pos])
            notake = rec(pos-1, n)

            return take+notake
        
        return rec(len(coins)-1, amount)

