class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        taken, mx, mn = set(), [], []
        for val in arrays[0]: 
            if val not in taken:
                taken.add(val)
                heappush(mn, val)
                heappush(mx, -val)

        res = 0
        for i in range(1, len(arrays)):
            row = arrays[i]

            for val in row: res = max(res, abs(val-mn[0]), abs(val+mx[0]))

            for val in row: 
                if val not in taken:
                    taken.add(val)
                    heappush(mn, val)
                    heappush(mx, -val)
        return res