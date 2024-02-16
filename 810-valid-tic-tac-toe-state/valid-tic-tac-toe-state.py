class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x, o = [], []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X': x.append(3*i + j)
                if board[i][j] == 'O': o.append(3*i + j)
                
        if (len(x) - len(o)) not in (0, 1): return False
        
        def getWins(positions):
            winningPositions = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ]
            return sum(all(i in positions for i in curr) for curr in winningPositions)
        
        x_wins = getWins(x)
        o_wins = getWins(o)
        
        if x_wins and o_wins: return False
        if x_wins > 2 or o_wins > 2: return False
        if x_wins and (len(x)-len(o)) == 0: return False 
        if o_wins and (len(x)-len(o)) == 1: return False

        return True