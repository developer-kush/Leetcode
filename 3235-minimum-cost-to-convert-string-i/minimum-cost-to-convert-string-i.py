class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[inf]*26 for _ in range(26)]

        for i in range(26): graph[i][i] = 0
        for x, y, z in zip(original, changed, cost):
            x, y = ord(x)-97, ord(y)-97
            graph[x][y] = min(graph[x][y], z)

        for m in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][m]+graph[m][j])
        
        tot = 0
        for a, b in zip(source, target):
            a, b = ord(a)-97, ord(b)-97
            if graph[a][b] == inf: return -1
            tot += graph[a][b]
        
        return tot