class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        indices = defaultdict(list)
        for idx, char in enumerate(ring): indices[char].append(idx)

        n = len(ring)
        def mindist(i1, i2):
            i1, i2 = min(i1, i2), max(i1, i2)
            df = i2 - i1
            db = i1 + n - i2
            return min(df, db)


        res = [(idx, 0) for idx in indices[key[-1]]]
        
        for i in range(len(key)-2, -1, -1):
            idxs = indices[key[i]]
            nr = []
            for idx in idxs:
                nr.append([idx, min(mindist(idx, other)+cost for other, cost in res)])
            res = nr

        ans = mindist(0, res[0][0]) + res[0][1]
        for i in range(1, len(res)): 
            ans = min(ans, mindist(0, res[i][0]) + res[i][1])

        return ans + len(key)