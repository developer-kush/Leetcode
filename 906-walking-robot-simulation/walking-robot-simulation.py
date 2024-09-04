class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        N, E, W, S = 'N', 'E', 'W', 'S'

        obstacles = set(tuple(row) for row in obstacles)

        res = 0
        x, y = 0, 0
        dir = N

        def left(x): return {N:W, W:S, S:E, E:N}[x]
        def right(x): return {N:E, E:S, S:W, W:N}[x]
        def cell(x, y, dir):
            if dir == N: return x, y+1
            if dir == S: return x, y-1
            if dir == E: return x+1, y
            if dir == W: return x-1, y

        for comm in commands:
            if comm == -2: dir = left(dir)
            if comm == -1: dir = right(dir)
            for _ in range(comm):
                p, q = cell(x, y, dir)
                if (p, q) in obstacles: break
                x, y = p, q

            res = max(res, x*x+y*y)

        return res