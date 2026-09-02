class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, index):
            # Base Case: All characters in the word have been successfully matched
            if index == len(word):
                return True

            # Boundary checks and character mismatch validation
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[index]:
                return False

            # Action: Mark the current cell as visited to prevent reuse
            temp = board[r][c]
            board[r][c] = "#"

            # Exploration: Check all 4 adjacent directions
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            # Backtrack: Restore the original character for other search paths
            board[r][c] = temp

            return found

        # Traverse the entire grid to find the starting letter
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
