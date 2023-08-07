from collections import defaultdict
def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        gridSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if ((board[i][j]) in rowSet[i]
                or (board[i][j]) in colSet[j]
                or (board[i][j]) in gridSet[(i // 3, j // 3)]):
                    return False
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                gridSet[(i // 3, j // 3)].add(board[i][j])
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))