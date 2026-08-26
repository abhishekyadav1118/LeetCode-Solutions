class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            # Base case: All queens are placed successfully
            if row == n:
                return 1

            count = 0
            for col in range(n):
                # Calculate diagonal identifiers
                d1 = row - col
                d2 = row + col

                # Check if the column or diagonals are already attacked
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue

                # Place the queen and mark placement
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                # Move to the next row
                count += backtrack(row + 1, cols, diag1, diag2)

                # Backtrack: Remove the queen to try other positions
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

            return count

        return backtrack(0, set(), set(), set())
