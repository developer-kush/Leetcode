class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        # print(ceil(hour), len(dist))
        if ceil(hour) < len(dist): return -1

        def isPossible(speed):
            h = 0
            for pt in dist:
                h = ceil(h) + pt/speed
            return h <= hour

        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo+hi)>>1
            if isPossible(mid): hi = mid
            else: lo = mid+1

        return lo