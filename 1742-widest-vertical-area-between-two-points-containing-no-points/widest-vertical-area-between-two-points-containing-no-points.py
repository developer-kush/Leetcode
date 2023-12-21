class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        values = sorted(set(x[0] for x in points))
        if len(values) < 2: return 0
        return max(values[i+1]-values[i] for i in range(len(values)-1))