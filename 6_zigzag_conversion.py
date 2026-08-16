class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base case: if 1 row or not enough characters to zigzag
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an empty string for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False

        # Traverse the string character by character
        for char in s:
            rows[current_row] += char

            # Change direction when hitting the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down based on current direction
            current_row += 1 if going_down else -1

        # Combine all rows to form the final result
        return "".join(rows)