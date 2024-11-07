class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ctr = [0]*25
        for c in candidates:
            for pos in range(25):
                if not c&1: ctr[pos]+=1
                c >>= 1
        return len(candidates)-min(ctr)