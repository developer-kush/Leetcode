class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        gded = [[0]*n for _ in range(m)]
        guards = set((x, y) for x, y in guards)
        walls = set((x, y) for x, y in walls)

        def fillGuards(gded, s1, e1, st1, s2, e2, st2, ver=False):
            if not ver:
                for i in range(s1, e1, st1):
                    curr = False
                    for j in range(s2, e2, st2):
                        if (i, j) in walls: curr = False
                        elif (i, j) in guards: curr = True
                        if curr: gded[i][j] = 1
                return 
            
            for i in range(s1, e1, st1):
                curr = False
                for j in range(s2, e2, st2):
                    if (j, i) in walls: curr = False
                    elif (j, i) in guards: curr = True
                    if curr: gded[j][i] = 1

        fillGuards(gded, 0, m, 1, 0, n, 1)
        fillGuards(gded, 0, m, 1, n-1, -1, -1)
        fillGuards(gded, 0, n, 1, 0, m, 1, ver = True)
        fillGuards(gded, 0, n, 1, m-1, -1, -1, ver = True)

        return sum(row.count(0) for row in gded) - len(walls)