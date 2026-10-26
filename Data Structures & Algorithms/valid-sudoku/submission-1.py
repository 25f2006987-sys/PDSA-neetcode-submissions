class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Validate Rows
        for row in board:
            tmp = [x for x in row if x != "."]
            if len(set(tmp)) < len(tmp):
                return False

        # 2. Validate Columns
        for col in range(9):
            tmp = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(set(tmp)) < len(tmp):
                return False

        # 3. Validate 9 Sub-boxes (Step by 3 for both row and col anchors)
        for r_anchor in range(0, 9, 3):
            for c_anchor in range(0, 9, 3):
                tmp = []
                # Gather all elements inside the current 3x3 block
                for r in range(r_anchor, r_anchor + 3):
                    for c in range(c_anchor, c_anchor + 3):
                        if board[r][c] != ".":
                            tmp.append(board[r][c])

                if len(set(tmp)) < len(tmp):
                    return False

        return True