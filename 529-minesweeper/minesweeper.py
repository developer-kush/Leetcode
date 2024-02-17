class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])

        def mineVal(i, j):
            return sum(
                (0<=r<n and 0<=c<m and board[r][c]=='M') 
                for r, c in [
                    [i-1,j-1],[i-1,j],[i-1,j+1], [i,j-1], 
                    [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1]
                ]
            )

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else: 
            q = deque([click])
            while q:
                r, c = q.popleft()
                if board[r][c] != 'E': continue
                cnt = mineVal(r, c)
                if cnt: 
                    board[r][c] = str(cnt); continue
                board[r][c] = 'B'
                for x, y in ((r-1, c), (r-1, c-1), (r-1, c+1), (r+1, c), (r+1, c-1), (r+1, c+1), (r, c-1), (r, c+1)):
                    if not (0<=x<n and 0<=y<m and board[x][y]=='E'): continue
                    q.append((x,y))

        return board