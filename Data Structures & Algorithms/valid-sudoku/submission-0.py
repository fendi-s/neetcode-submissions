class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in range(9):
            seen = set()
            for i in range(9):
                row_val = board[row][i]
                if row_val == ".":
                    continue
                if row_val in seen:
                    return False
                seen.add(row_val)

        # collumns
        for coll in range(9):
            seen = set()
            for j in range(9):
                coll_val = board[j][coll]
                if coll_val == ".":
                    continue
                if coll_val in seen:
                    return False
                seen.add(coll_val)

        # sub-box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    coll = (square % 3) * 3 + j
                    val = board[row][coll]
                    if val == ".":
                        continue
                    elif val in seen:
                        return False
                    seen.add(val)

        return True
