class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        lidx = {0: -1}
        res = tiring = 0

        for idx, val in enumerate(hours):
            if val > 8: tiring += 1
            else: tiring -= 1

            if tiring-1 in lidx: res = max(res, idx-lidx[tiring-1])
            if tiring > 0: res = max(res, idx + 1)

            if tiring not in lidx: lidx[tiring] = idx
        
        return res