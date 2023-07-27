class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n == 1: return sum(batteries)
        if len(batteries) == n: return min(batteries)

        batteries = sorted(batteries, reverse=True)
        first, last = batteries[:n], batteries[n:]
        remsum = sum(last)
        
        
        def isPossible(time):
            tot = 0
            for i in first: tot += max(time-i, 0)
            return tot <= remsum

        lo, hi = 0, sum(batteries)//n
        while lo<hi:
            mid = (lo+hi+1)//2
            if isPossible(mid): lo = mid
            else: hi = mid-1
        
        return lo
