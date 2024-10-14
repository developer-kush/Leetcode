class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mxprof, mn = 0, float('inf')

        mem = list(prices)
        for i in range(n):
            mxprof = max(mxprof, prices[i]-mn)
            mem[i] = mxprof
            mn = min(mn, prices[i])
        
        res = mx = 0
        for i in range(n-1, -1, -1):
            res = max(res, mx-prices[i] + (mem[i-1] if i else 0))
            mx = max(mx, prices[i])
        
        return res