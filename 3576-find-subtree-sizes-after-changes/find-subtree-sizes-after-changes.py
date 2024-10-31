class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        c = defaultdict(list)
        for i in range(n): c[parent[i]].append(i)
        root = c[-1][0]
        par = {}
        
        def rec(root):
            nonlocal par
            curr = s[root]
            f = False
            if curr in par: f = True
            if f: parent[root] = par[curr]
            if f: x = par[curr]
            par[curr] = root
            for ne in c[root]: rec(ne)
            if f: par[curr] = x
            else: del par[curr]
        rec(root)

        res = [0]*n
        c = defaultdict(list)
        for i in range(n): c[parent[i]].append(i)
        def rec(root):
            nonlocal res
            tot = 1
            for ne in c[root]: tot+=rec(ne)
            res[root] = tot
            return tot
        rec(c[-1][0])
        return res