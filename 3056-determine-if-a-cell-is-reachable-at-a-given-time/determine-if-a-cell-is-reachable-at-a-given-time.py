class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy: return t!=1
        x, y = abs(sx-fx), abs(sy-fy)
        return t >= x and t >= y