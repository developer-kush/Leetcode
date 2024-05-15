class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return 0
        n, m = len(grid), len(grid[0])
    
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]: q.append((i,j,1))
                    
        while q:
            x, y, dist = q.popleft()
            for i, j in ((x+1,y), (x,y+1),(x-1,y),(x,y-1)):
                if 0<=i<n and 0<=j<m and grid[i][j] == 0: 
                    grid[i][j] = dist+1
                    q.append((i,j,dist+1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]: grid[i][j] -= 1
        
        hp = [(-grid[0][0],(0,0))]
        visited = set([(0,0)])
        res = grid[0][0]
        while hp:
            val, pos = heappop(hp)
            x,y = pos
            res = min(res, grid[x][y])
            for i,j in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
                if 0<=i<n and 0<=j<m and (i,j) not in visited:
                    if (i,j) == (n-1,m-1): return min(-val, grid[i][j])
                    visited.add((i,j))
                    heappush(hp,(-min(-val, grid[i][j]), (i,j)))
                    
        return res
        
            
            
            
        # for row in grid: print(*row)
        # print()
        
        # return rec(n-1, m-1)
    