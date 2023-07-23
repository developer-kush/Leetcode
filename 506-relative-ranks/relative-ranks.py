from heapq import heappush, heappop, heapify

class Solution:
    def findRelativeRanks(self, sc: List[int]) -> List[str]:
        
        hp = [[-i,idx] for idx,i in enumerate(sc)]
        heapify(hp)

        sc[heappop(hp)[1]] = "Gold Medal"
        if not hp: return sc
        sc[heappop(hp)[1]] = "Silver Medal"
        if not hp: return sc
        sc[heappop(hp)[1]] = "Bronze Medal"

        for i in range(len(hp)):
            sc[heappop(hp)[1]] = str(4+i)
        
        return sc
        