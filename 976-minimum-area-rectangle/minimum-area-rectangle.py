class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for x, y in points: d[x].append(y)

        lineSets = defaultdict(list)

        for x, grp in d.items(): 
            grp.sort()
            for i in range(len(grp)):
                for j in range(i+1, len(grp)):
                    lineSets[(grp[i], grp[j])].append(x)

        res = float('inf')
        for (x, y), grp in lineSets.items():
            grp.sort()
            for i in range(1, len(grp)):
                res = min(res, (y-x)*(grp[i]-grp[i-1]))
        
        return res if res != float('inf') else 0