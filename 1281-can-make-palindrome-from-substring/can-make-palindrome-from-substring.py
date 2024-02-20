class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        qstarts = set(query[0]-1 for query in queries)
        res = [0]*len(queries)

        reqmap = defaultdict(list)
        for idx, (st, e, k) in enumerate(queries): reqmap[e].append((st, k, idx))

        counts = {}
        ctr = Counter()
        if -1 in qstarts: counts[-1] = dict(ctr)

        for i in range(len(s)):
            ctr[s[i]] += 1
            if i in qstarts: counts[i] = dict(ctr)
            
            for st, k, idx in reqmap[i]:
                cs = counts[st-1]
                diffs = sum((ctr[chr(ch)]-cs.get(chr(ch), 0))&1 for ch in range(97, 97+26))
                res[idx] = (diffs >> 1) <= k

        return res