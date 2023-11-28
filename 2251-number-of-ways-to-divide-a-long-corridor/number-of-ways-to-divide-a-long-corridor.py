class Solution:
    def numberOfWays(self, corridor: str) -> int:
        corridor = corridor.strip("P")
        if not corridor: return 0

        MOD = int(1e9 + 7)
        tot = last = 1
        cnt = 0

        for i in corridor:
            if i == 'P': 
                if cnt and not cnt&1: last += 1
            if i == 'S':
                cnt += 1
                if cnt&1:
                    tot = (tot*last)%MOD
                    last = 1

        if cnt&1: return 0
        return tot 