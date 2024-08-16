class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        taken, mx, mn = set(), [], []

        res = 0
        for row in arrays:

            for val in row:
                if not mn: continue
                res = max(res, abs(val-mn[0]), abs(val+mx[0]))

            for val in row: 
                if val not in taken:
                    taken.add(val)
                    heappush(mn, val)
                    heappush(mx, -val)
        return res