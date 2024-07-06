class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= ((n-1)<<1)
        if time == 0: return 1
        if time < n: return time + 1
        return n - (time - n + 1)