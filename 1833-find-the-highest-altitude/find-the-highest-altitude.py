class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = altitude = 0
        for i in gain: 
            altitude += i
            res = max(res, altitude)
        return res



#  -5 1 5 0 -7
# -------------
# -------------
# -------------
# -------------
# -------------
# -------------
# -------------
# -------------
# -------------