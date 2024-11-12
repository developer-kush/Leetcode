class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # items.append([inf, 0])

        maxvals = {}
        mx = 0
        for p, b in sorted(items):
            mx = max(mx, b)
            maxvals[p] = mx

        uniq = sorted(set(p for p, q in items))

        res = []
        for q in queries:
            pos = bisect_left(uniq, q+1)
            if pos == 0: res.append(0)
            else: res.append(maxvals[uniq[pos-1]])
        
        return res