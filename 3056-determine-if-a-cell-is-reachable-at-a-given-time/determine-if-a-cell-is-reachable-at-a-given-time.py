class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x, y = abs(sx-fx), abs(sy-fy)
        dist = max(x,y)
        if sx == fx and sy == fy: return t!=1
        return t>=dist
        