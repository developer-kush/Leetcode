class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
    
        diffs = [[i+j,i,j] for i,j in zip(aliceValues, bobValues)]
        
        diffs = reversed(sorted( diffs ))

        tot = 0
        for i, val in enumerate(diffs):
            if not i&1: tot += val[1]
            else: tot -= val[2]
        
        if tot > 0: return 1
        if tot < 0: return -1
        return 0