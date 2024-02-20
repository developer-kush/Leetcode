class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        def setCount(n):
            tot = 0
            while n:
                tot += 1
                n = n & (n-1)
            return tot

        qstarts = set(query[0]-1 for query in queries)
        res = [0]*len(queries)

        reqmap = defaultdict(list)
        for idx, (st, e, k) in enumerate(queries): reqmap[e].append((st, k, idx))

        counts = {}
        ctr = 0
        if -1 in qstarts: counts[-1] = 0

        for i in range(len(s)):
            ctr = ctr ^ (1 << (ord(s[i])-97))
            
            if i in qstarts: counts[i] = ctr
            
            for st, k, idx in reqmap[i]:
                cs = counts[st-1]
                diffs = setCount(ctr ^ cs)
                res[idx] = (diffs >> 1) <= k

        return res