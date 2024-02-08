class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        if board == [[1, 2, 3], [4, 5, 0]]: return 0
        
        board = board[0] + board[1]
        movemaps = {
            0 : [1, 3],
            1 : [0, 2, 4],
            2 : [1, 5],
            3 : [0, 4],
            4 : [1, 3, 5],
            5 : [2, 4],
        }

        q = deque([[0, board.index(0), board]])
        visited = set([str(board)])

        while q:
            dist, pos, board = q.popleft()
            for ne in movemaps[pos]:
                cpboard = list(board)
                cpboard[pos], cpboard[ne] = cpboard[ne], cpboard[pos]
                if ''.join(map(str, cpboard)) == '123450': return dist + 1
                if str(cpboard) in visited: continue
                visited.add(str(cpboard))
                q.append([dist+1, ne, cpboard])
    
        return -1