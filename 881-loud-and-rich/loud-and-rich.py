class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        for u, v in richer: graph[v].append(u)
        
        n = len(quiet)
        ans = [-1]*n

        def rec(node):
            if ans[node] != -1: return ans[node]
            res = node
            for ne in graph[node]:
                sol = rec(ne)
                res = min([res, sol], key = lambda x: quiet[x])
            ans[node] = res
            return res

        for i in range(n): ans[i] = rec(i)

        return ans