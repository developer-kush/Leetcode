class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        ptr = 0
        for s, e in firstList:
            if ptr >= len(secondList): break
            while ptr < len(secondList) and secondList[ptr][0] <= e:
                u, v = secondList[ptr]
                if v < s: ptr += 1; continue
                res.append([max(s, u), min(e, v)])
                if v < e: ptr += 1
                else: break
        
        return res