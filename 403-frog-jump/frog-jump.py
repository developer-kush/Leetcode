class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = { 0: set([0]) }
        sset = set(stones)
        target = stones[-1]

        for stone in stones:
            if stone not in reachable: continue
            for k in list(reachable[stone]):
                if abs(target - stone - k) <= 1 : return True
                if stone+k+1 in sset:
                    if stone+k+1 not in reachable: reachable[stone+k+1] = set()
                    reachable[stone+k+1].add(k+1)
                if stone+k in sset:
                    if stone+k not in reachable: reachable[stone+k] = set()
                    if k: reachable[stone+k].add(k)
                if stone+k-1 in sset:
                    if stone+k-1 not in reachable: reachable[stone+k-1] = set()
                    if k-1: reachable[stone+k-1].add(k-1)
        
        return False
        
