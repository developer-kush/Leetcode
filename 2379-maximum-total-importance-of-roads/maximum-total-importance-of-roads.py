class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = Counter()
        for u, v in roads:
            deg[u] += 1
            deg[v] += 1
        deg = sorted(deg.values(), reverse = True)
        deg += [0]*(n-len(deg))

        return sum(cnt*val for cnt, val in zip(range(n, 0, -1), deg))