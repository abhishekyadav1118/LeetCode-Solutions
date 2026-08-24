class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val != ".":
                    # Create unique string representations for each constraint
                    row_key = f"row {r} has {val}"
                    col_key = f"col {c} has {val}"
                    box_key = f"box {r // 3}-{c // 3} has {val}"

                    # If any key is already in the set, the board is invalid
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False

                    # Add constraints to the tracking set
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)

        return True
