class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for rows
        for i in range(9):
            sets = set()
            for j in range (9):  
                if board[i][j] in sets:
                    return False
                elif board[i][j] != ".":
                    sets.add(board[i][j])
        #for cols
        for i in range(9):
            sets = set()
            for j in range(9):
                if board[j][i] in sets:
                    return False
                elif board[j][i] != ".":
                    sets.add(board[j][i])

        #for Box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    cols = (square % 3) * 3 + j

                    if board[row][cols] in seen:
                        return False
                    elif board[row][cols] != ".":
                        seen.add(board[row][cols])
        return True
# TC = O(n^2) SC = O(n)
                