class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        lidx = {0: -1}
        res = tiring = 0

        for idx, val in enumerate(hours):
            if val > 8: tiring += 1
            else: tiring -= 1
            hours[idx] = tiring
            if tiring not in lidx: lidx[tiring] = idx
        
        clidx = inf
        for key in sorted(lidx):
            clidx = min(clidx, lidx[key])
            lidx[key] = clidx
        srtkey = sorted(lidx)
            
        for idx, val in enumerate(hours):
            if val-1 < srtkey[0]: continue
            pos = bisect_left(srtkey, val-1)
            res = max(res, idx-lidx[srtkey[pos]])
        
        return res