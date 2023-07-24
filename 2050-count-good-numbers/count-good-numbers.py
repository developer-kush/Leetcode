class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = operator.pow(10, 9) + 7

        def fastPow(x, p):
            if p == 0: return 1
            
            res = fastPow(x, p>>1)
            if p&1: return (res*res*x)%MOD
            return res*res %MOD
    
        oddCount = evenCount = n>>1
        if n&1: evenCount+=1

        return fastPow(4, oddCount)*fastPow(5, evenCount)%MOD