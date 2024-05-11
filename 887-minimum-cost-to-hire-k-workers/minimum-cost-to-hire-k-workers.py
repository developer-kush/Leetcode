class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)

        wpq = sorted([ [w/q, q] for w, q in zip(wage, quality) ])
        
        hp = []
        s = 0
        for i in range(k):
            unit_wage, quality = wpq[i]
            s += quality
            heappush(hp, -quality)

        res = s*unit_wage

        for i in range(k, n):
            unit_wage, quality = wpq[i]
            heappush(hp, -quality)
            s += quality + heappop(hp)
            res = min(res, s*unit_wage)

        return res