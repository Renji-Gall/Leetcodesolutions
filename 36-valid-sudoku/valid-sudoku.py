class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    continue
                if (board[y][x] in row[y] or board[y][x] in col[x] or board[y][x] in square[(y // 3, x // 3)]):
                    return False
                
                col[x].add(board[y][x])
                row[y].add(board[y][x])
                square[(y // 3, x // 3)].add(board[y][x])
        return True