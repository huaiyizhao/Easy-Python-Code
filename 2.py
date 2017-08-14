#判断数独是否合法
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            I = []
            J = []
            X = []
            Y = []
            for j in range(9):
                if(board[i][j] != '.'):
                    if (int(board[i][j]) >= 0) and (int(board[i][j]) <= 9):
                        I.append(board[i][j])
                if(board[j][i] != '.'):
                    if (int(board[j][i]) >= 0) and (int(board[j][i]) <= 9):
                        J.append(board[j][i])
            [X.append(m) for m in I if not m in X]
            [Y.append(n) for n in J if not n in Y]
            if (X != I) or (Y != J):
                return False
        for k in range(9):
            K = []
            P = []
            for i in range((k % 3) * 3, (k % 3) * 3 + 3):
                for j in range((k / 3) * 3, (k / 3) * 3 + 3):
                    if(board[i][j] != '.') and (int(board[i][j]) >=0) and (int(board[i][j]) <= 9):
                        K.append(board[i][j])
            [P.append(p) for p in K if not p in P]
            if K != P:
                return False
            
        return True
            
