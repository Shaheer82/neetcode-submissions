class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            row_set = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in row_set:
                        return False
                    row_set.add(val)

        # Check columns
        for c in range(9):
            col_set = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in col_set:
                        return False
                    col_set.add(val)

        # Check 3x3 boxes
        for l in range(0, 9, 3):
            m = l
            n = l+3
            for k in range(0, 9, 3):
                x = k
                y = k+3
                num_list = []
                for i in range(m, n):
                    for j in range(x, y):
                        if board[i][j] != ".":
                            if board[i][j] not in num_list:
                                num_list.append(board[i][j])
                            else:
                                return False
        return True