class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cost = defaultdict(lambda: defaultdict(lambda: float('inf')))

        q = [(0, n-1, m-1)]
        vis = set()
        while q:
            d, x, y = heappop(q)
            if (x, y) in vis: continue
            vis.add((x, y))
            cost[x][y] = min(d, cost[x][y])
            for a, (b, c) in {1:(x, y-1), 3:(x-1, y), 2:(x, y+1), 4:(x+1, y)}.items():
                if not (0<=b<n and 0<=c<m): continue
                if (b, c) in vis: continue
                if grid[b][c] == a: heappush(q, (d, b, c))
                else:heappush(q, (d+1, b, c))

        return cost[0][0]