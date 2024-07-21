class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def getOrder(conditions):
            nxtnums = defaultdict(set)
            for u, v in conditions: 
                nxtnums[u].add(v)
            
            reqCtr = Counter()

            nullvals = set(range(1, k+1))

            for row in nxtnums.values():
                for val in row: 
                    cnt = reqCtr[val]
                    if val in nullvals: nullvals.remove(val)
                    reqCtr[val] += 1
            
            cnt = k
            order = []
            while cnt:
                row = nullvals

                if not row: return []

                numDrops = Counter()

                for val in row:
                    order.append(val)
                    cnt -= 1
                    for num in nxtnums[val]: numDrops[num] += 1
                
                nullvals = set()
                
                for num, val in numDrops.items():
                    ccnt = reqCtr[num]
                    reqCtr[num] -= val
                    if reqCtr[num] == 0: nullvals.add(num)
        
            return order


        row = col = None

        row = getOrder(rowConditions)
        if not row: return []
        col = getOrder(colConditions)
        if not col: return []

        coords = [[0]*2 for _ in range(k+1)]
        res = [[0]*k for _ in range(k)]
        for i in range(k):
            coords[row[i]][0] = i
            coords[col[i]][1] = i
        for idx, (u, v) in enumerate(coords):
            res[u][v] = idx

        return res