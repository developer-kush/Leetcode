class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        ends = []

        mx = float('-inf')
        lastv = -1
        for _, v, w in sorted(events, key=lambda x: x[1]):
            if v != lastv: ends.append((lastv, mx))
            mx = max(mx, w)
            lastv = v
        ends.append((v, mx))

        res = mx = 0
        for u, _, w in sorted(events, reverse = True):
            while ends[-1][0] >= u: ends.pop()
            mx = max(mx, w)
            res = max(res, mx+ends[-1][1])

        return max(res, max(w for u, v, w in events))