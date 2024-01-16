class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        res = n-1

        def getIncSum(ln, x):
            curr, tot = 1, 0
            for _ in range(ln):
                tot += curr
                curr *= x
                if tot > n: break
            return tot
        
        def getBest(size):
            lo, hi = 2, int(1e18)
            while lo < hi:
                mid = (lo+hi)>>1
                cost = getIncSum(size, mid)
                if cost == n: return mid
                if cost > n: hi = mid
                if cost < n: lo = mid+1
            
            cost = getIncSum(size, lo)
            if cost != n: return float('inf')
            return lo
            

        for i in range(3, 100):
            curr = getBest(i)
            if res!=float('inf'): res = min(res, curr)

        return str(res)

"""

"""