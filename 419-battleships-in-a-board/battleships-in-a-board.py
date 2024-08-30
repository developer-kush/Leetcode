class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.': continue
                if i and board[i-1][j] == 'X': continue
                if j and board[i][j-1] == 'X': continue
                cnt += 1
        return cnt