class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1: return 0
        
        @cache
        def rec(ch, cp):

            if ch > n: return float('inf')
            if ch == n: return 0
            
            return min(
                rec(ch*2, ch)+2, 
                rec(ch+cp, cp)+1
            )

        return rec(1, 1)+1