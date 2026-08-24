class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Track used digits in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Step 1: Populate current state and store all empty cell positions
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))

        # Step 2: Recursive backtracking function
        def backtrack(cell_idx: int) -> bool:
            # If all empty cells are filled, a solution is found
            if cell_idx == len(empty_cells):
                return True

            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)

            # Try placing digits 1-9
            for digit in "123456789":
                if (
                    digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box_idx]
                ):
                    # Place the digit and update sets
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    # Move to the next empty cell
                    if backtrack(cell_idx + 1):
                        return True

                    # Backtrack (Undo placement)
                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)
